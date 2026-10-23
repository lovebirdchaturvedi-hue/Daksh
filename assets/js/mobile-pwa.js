/**
 * APD GLOBAL TRADE - PWA & MOBILE APP ENGINE
 * Features:
 * 1. Automatic Service Worker Registration
 * 2. 1-Tap Native Install Prompt (Android/Chrome/Edge/Desktop)
 * 3. iOS Safari Add-To-Home-Screen Guidance Modal
 * 4. Institutional 5-Tab Mobile Bottom App Bar (Home, Live RFQs, Plans, Portal, Trade Desk)
 * 5. Screen overflow prevention & floating widget offset
 */

(function () {
  'use strict';

  // 1. REGISTER SERVICE WORKER
  if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
      navigator.serviceWorker
        .register('/sw.js')
        .then((reg) => {
          console.log('[APD PWA] Service Worker registered with scope:', reg.scope);
        })
        .catch((err) => {
          console.warn('[APD PWA] Service Worker registration failed:', err);
        });
    });
  }

  // 2. CHECK STANDALONE MODE
  const isStandalone =
    window.matchMedia('(display-mode: standalone)').matches ||
    window.navigator.standalone === true;

  if (isStandalone) {
    document.documentElement.classList.add('apd-standalone-app');
  }

  // 3. PWA INSTALL PROMPT CONTROLLER
  let deferredPrompt = null;

  window.addEventListener('beforeinstallprompt', (e) => {
    // Prevent the default browser mini-infobar
    e.preventDefault();
    deferredPrompt = e;
    console.log('[APD PWA] Captured beforeinstallprompt event');

    // Show floating install banner unless user dismissed it in this session
    if (!isStandalone && !sessionStorage.getItem('apd_pwa_banner_dismissed')) {
      showInstallBanner();
    }

    // Enable any custom install buttons across pages
    document.querySelectorAll('.pwa-install-trigger').forEach((btn) => {
      btn.style.display = 'inline-flex';
      btn.addEventListener('click', triggerPwaInstall);
    });
  });

  window.addEventListener('appinstalled', () => {
    console.log('[APD PWA] App installed successfully');
    hideInstallBanner();
    deferredPrompt = null;
    showToast('🎉 APD Global Trade App Installed Successfully!');
  });

  function triggerPwaInstall() {
    if (deferredPrompt) {
      deferredPrompt.prompt();
      deferredPrompt.userChoice.then((choiceResult) => {
        if (choiceResult.outcome === 'accepted') {
          console.log('[APD PWA] User accepted install prompt');
        } else {
          console.log('[APD PWA] User dismissed install prompt');
        }
        deferredPrompt = null;
        hideInstallBanner();
      });
    } else {
      // Check for iOS
      const isIOS = /iPad|iPhone|iPod/.test(navigator.userAgent) && !window.MSStream;
      if (isIOS) {
        showIosInstructionsModal();
      } else {
        showToast('ℹ️ To install: Open browser menu (⋮) and tap "Install app" or "Add to Home screen"');
      }
    }
  }

  function showInstallBanner() {
    if (document.getElementById('apd-pwa-install-banner') || isStandalone) return;

    const banner = document.createElement('div');
    banner.id = 'apd-pwa-install-banner';
    banner.innerHTML = `
      <div class="apd-pwa-content">
        <div class="apd-pwa-icon">
          <img src="/assets/icons/icon-192.png" alt="APD App" width="38" height="38" style="border-radius:10px;">
        </div>
        <div class="apd-pwa-text">
          <div class="apd-pwa-title">APD Global Trade App</div>
          <div class="apd-pwa-subtitle">Instant Buyer Inquiries • Live RFQs • Fast Portal</div>
        </div>
        <div class="apd-pwa-actions">
          <button id="apd-pwa-btn-install" class="apd-pwa-install-btn">Install App</button>
          <button id="apd-pwa-btn-close" class="apd-pwa-close-btn" aria-label="Dismiss">✕</button>
        </div>
      </div>
    `;

    document.body.appendChild(banner);

    document.getElementById('apd-pwa-btn-install').addEventListener('click', () => {
      triggerPwaInstall();
    });

    document.getElementById('apd-pwa-btn-close').addEventListener('click', () => {
      hideInstallBanner();
      sessionStorage.setItem('apd_pwa_banner_dismissed', '1');
    });
  }

  function hideInstallBanner() {
    const banner = document.getElementById('apd-pwa-install-banner');
    if (banner) {
      banner.style.opacity = '0';
      banner.style.transform = 'translateY(100%)';
      setTimeout(() => banner.remove(), 300);
    }
  }

  function showIosInstructionsModal() {
    let modal = document.getElementById('apd-ios-pwa-modal');
    if (!modal) {
      modal = document.createElement('div');
      modal.id = 'apd-ios-pwa-modal';
      modal.innerHTML = `
        <div class="apd-ios-modal-backdrop"></div>
        <div class="apd-ios-modal-box">
          <div style="font-size:32px; margin-bottom:10px;">📲</div>
          <h3 style="color:#fff; font-size:18px; font-weight:800; margin-bottom:8px;">Install APD Trade on iPhone / iPad</h3>
          <p style="color:#94a3b8; font-size:13px; line-height:1.6; margin-bottom:18px;">
            Enjoy instant full-screen access to Live RFQs and the Trade Desk without opening Safari each time:
          </p>
          <div style="background:rgba(255,255,255,0.05); border:1px solid rgba(212,175,55,0.3); border-radius:12px; padding:14px; text-align:left; font-size:13px; color:#cbd5e1; margin-bottom:18px;">
            <div style="margin-bottom:8px;">1. Tap the <b>Share</b> button <span style="font-size:16px;">⎋</span> at the bottom of Safari.</div>
            <div style="margin-bottom:8px;">2. Scroll down and tap <b>'Add to Home Screen'</b> <span style="font-size:16px;">⊞</span>.</div>
            <div>3. Tap <b>'Add'</b> in the top-right corner.</div>
          </div>
          <button id="apd-ios-modal-close" style="background:var(--gold,#d4af37); color:#000; border:none; font-weight:900; font-size:14px; padding:12px 28px; border-radius:50px; cursor:pointer; width:100%;">Got It</button>
        </div>
      `;
      document.body.appendChild(modal);
      modal.querySelector('#apd-ios-modal-close').addEventListener('click', () => modal.remove());
      modal.querySelector('.apd-ios-modal-backdrop').addEventListener('click', () => modal.remove());
    }
  }

  function showToast(message) {
    const toast = document.createElement('div');
    toast.className = 'apd-toast-notification';
    toast.textContent = message;
    document.body.appendChild(toast);
    setTimeout(() => {
      toast.classList.add('show');
    }, 50);
    setTimeout(() => {
      toast.classList.remove('show');
      setTimeout(() => toast.remove(), 400);
    }, 4000);
  }

  // 4. INJECT INSTITUTIONAL 5-TAB MOBILE BOTTOM APP BAR
  function injectMobileBottomBar() {
    if (document.getElementById('apd-mobile-bottom-bar')) return;

    // Detect active tab from pathname
    const path = window.location.pathname.toLowerCase();
    const isHome = path === '/' || path.endsWith('/index.html') || path === '';
    const isRFQs = path.includes('public-rfqs') || path.includes('buyer-rfqs');
    const isPlans = path.includes('membership');
    const isPortal = path.includes('supplier-login') || path.includes('login') || path.includes('dashboard') || path.includes('admin');

    const bottomBar = document.createElement('nav');
    bottomBar.id = 'apd-mobile-bottom-bar';
    bottomBar.setAttribute('aria-label', 'Mobile Navigation');
    bottomBar.innerHTML = `
      <a href="/" class="apd-tab-item ${isHome ? 'active' : ''}">
        <span class="apd-tab-icon">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
        </span>
        <span class="apd-tab-label">Home</span>
      </a>

      <a href="/public-rfqs.html" class="apd-tab-item ${isRFQs ? 'active' : ''}">
        <span class="apd-tab-icon" style="position:relative;">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>
          <span class="apd-tab-badge">24+</span>
        </span>
        <span class="apd-tab-label">Live RFQs</span>
      </a>

      <a href="/membership.html" class="apd-tab-item ${isPlans ? 'active' : ''}">
        <span class="apd-tab-icon">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="7"></circle><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"></polyline></svg>
        </span>
        <span class="apd-tab-label">Plans</span>
      </a>

      <a href="/supplier-login.html" class="apd-tab-item ${isPortal ? 'active' : ''}">
        <span class="apd-tab-icon">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="11" x="3" y="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
        </span>
        <span class="apd-tab-label">Portal</span>
      </a>

      <a href="https://wa.me/919266418868?text=Hello%20APD%20Global%20Trade%20Desk%2C%20I%20need%20assistance%20with%20commodities%20and%20orders" target="_blank" rel="noopener noreferrer" class="apd-tab-item apd-desk-tab">
        <span class="apd-tab-icon">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg>
        </span>
        <span class="apd-tab-label">Desk</span>
      </a>
    `;

    document.body.appendChild(bottomBar);

    // Hide any legacy 2-button action bar so it doesn't clash
    const oldBar = document.getElementById('mobileActionBar');
    if (oldBar) {
      oldBar.style.display = 'none';
    }
  }

  // 5. INJECT PWA STYLESHEET
  function injectPwaStyles() {
    if (document.getElementById('apd-pwa-styles')) return;

    const style = document.createElement('style');
    style.id = 'apd-pwa-styles';
    style.textContent = `
      /* PWA Floating Install Banner */
      #apd-pwa-install-banner {
        position: fixed;
        bottom: 74px;
        left: 12px;
        right: 12px;
        z-index: 99998;
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.96), rgba(2, 6, 23, 0.98));
        border: 1px solid rgba(212, 175, 55, 0.4);
        border-radius: 16px;
        padding: 10px 14px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.7), 0 0 20px rgba(212, 175, 55, 0.2);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      }
      .apd-pwa-content {
        display: flex;
        align-items: center;
        gap: 12px;
      }
      .apd-pwa-icon {
        flex-shrink: 0;
        display: flex;
        align-items: center;
      }
      .apd-pwa-text {
        flex: 1;
        min-width: 0;
      }
      .apd-pwa-title {
        font-size: 13.5px;
        font-weight: 800;
        color: #fff;
        line-height: 1.2;
      }
      .apd-pwa-subtitle {
        font-size: 11px;
        color: #94a3b8;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
      }
      .apd-pwa-actions {
        display: flex;
        align-items: center;
        gap: 6px;
        flex-shrink: 0;
      }
      .apd-pwa-install-btn {
        background: linear-gradient(135deg, #d4af37, #b8860b);
        color: #020617;
        font-weight: 900;
        font-size: 12px;
        padding: 7px 15px;
        border-radius: 20px;
        border: none;
        cursor: pointer;
        box-shadow: 0 2px 8px rgba(212,175,55,0.4);
        white-space: nowrap;
      }
      .apd-pwa-close-btn {
        background: transparent;
        color: #64748b;
        border: none;
        font-size: 14px;
        padding: 4px 6px;
        cursor: pointer;
      }

      /* Desktop & Mobile Display Adjustments for PWA Banner */
      @media (min-width: 769px) {
        #apd-pwa-install-banner {
          bottom: 25px;
          left: auto;
          right: 25px;
          width: 380px;
        }
      }

      /* 5-Tab Mobile Bottom Navigation Bar */
      #apd-mobile-bottom-bar {
        display: none;
      }

      @media (max-width: 768px) {
        #apd-mobile-bottom-bar {
          display: flex !important;
          position: fixed !important;
          bottom: 0 !important;
          left: 0 !important;
          right: 0 !important;
          width: 100% !important;
          height: 64px !important;
          background: rgba(2, 6, 23, 0.94) !important;
          backdrop-filter: blur(20px) !important;
          -webkit-backdrop-filter: blur(20px) !important;
          border-top: 1px solid rgba(212, 175, 55, 0.25) !important;
          z-index: 99999 !important;
          justify-content: space-around !important;
          align-items: center !important;
          padding: 0 4px !important;
          box-shadow: 0 -8px 25px rgba(0, 0, 0, 0.7) !important;
          box-sizing: border-box !important;
        }

        /* Pad body so content is never covered */
        body {
          padding-bottom: 74px !important;
        }

        /* Move floating WhatsApp & Suhana Sales Bot cleanly above bottom bar */
        #suhana-bot-container,
        .float-wa,
        .float.whatsapp,
        [style*="position: fixed; bottom: 30px;"],
        [style*="position: fixed; bottom: 25px;"],
        [style*="position: fixed; bottom: 20px;"] {
          bottom: 76px !important;
        }

        .apd-tab-item {
          display: flex !important;
          flex-direction: column !important;
          align-items: center !important;
          justify-content: center !important;
          flex: 1 !important;
          height: 100% !important;
          text-decoration: none !important;
          color: #94a3b8 !important;
          transition: all 0.2s ease !important;
          -webkit-tap-highlight-color: transparent !important;
        }

        .apd-tab-item.active {
          color: #d4af37 !important;
        }

        .apd-tab-icon {
          display: flex;
          align-items: center;
          justify-content: center;
          margin-bottom: 3px;
          transition: transform 0.2s;
        }

        .apd-tab-item.active .apd-tab-icon {
          transform: translateY(-2px);
          color: #d4af37;
        }

        .apd-tab-label {
          font-size: 10px !important;
          font-weight: 700 !important;
          letter-spacing: 0.2px !important;
        }

        .apd-tab-badge {
          position: absolute;
          top: -4px;
          right: -8px;
          background: #ef4444;
          color: #fff;
          font-size: 8px;
          font-weight: 900;
          padding: 1px 4px;
          border-radius: 8px;
          animation: pulse 1.5s infinite;
        }

        .apd-desk-tab {
          color: #22c55e !important;
        }
      }

      /* iOS Modal */
      #apd-ios-pwa-modal {
        position: fixed;
        inset: 0;
        z-index: 100000;
        display: flex;
        align-items: flex-end;
        justify-content: center;
        padding-bottom: 20px;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      }
      .apd-ios-modal-backdrop {
        position: absolute;
        inset: 0;
        background: rgba(0,0,0,0.7);
        backdrop-filter: blur(5px);
      }
      .apd-ios-modal-box {
        position: relative;
        background: #0f172a;
        border: 1px solid rgba(212,175,55,0.4);
        border-radius: 20px;
        padding: 24px;
        width: 90%;
        max-width: 400px;
        text-align: center;
        box-shadow: 0 20px 50px rgba(0,0,0,0.8);
      }

      /* Toast Notification */
      .apd-toast-notification {
        position: fixed;
        top: 20px;
        left: 50%;
        transform: translateX(-50%) translateY(-100px);
        background: #0f172a;
        border: 1px solid #d4af37;
        color: #fff;
        font-size: 13px;
        font-weight: 700;
        padding: 12px 24px;
        border-radius: 30px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.6);
        z-index: 999999;
        transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        pointer-events: none;
      }
      .apd-toast-notification.show {
        transform: translateX(-50%) translateY(0);
      }
    `;
    document.head.appendChild(style);
  }

  // Initialize once DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
      injectPwaStyles();
      injectMobileBottomBar();
    });
  } else {
    injectPwaStyles();
    injectMobileBottomBar();
  }
})();
