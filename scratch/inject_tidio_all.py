import glob
import os

tidio_snippet = """
<style>
  /* Force Tidio Chat widget to left side so it never covers WhatsApp floating button */
  #tidio-chat, #tidio-chat-iframe, iframe[title="Tidio Chat"], div[id^="tidio-chat"] {
      left: 20px !important;
      right: auto !important;
  }
</style>
<script id="tidio-auto-open">
  document.addEventListener("tidioChat-ready", function() {
      setTimeout(function() {
          try {
              window.tidioChatApi.open();
              const el = document.getElementById("tidio-chat") || document.getElementById("tidio-chat-iframe") || document.querySelector("iframe[title='Tidio Chat']");
              if (el) { el.style.left = "20px"; el.style.right = "auto"; }
          } catch(e){}
      }, 2000);
  });
</script>

<script src="//code.tidio.co/zs195w58z0vrzcknn4gkbosvrnn63xfe.js" async></script>
"""

pages_to_update = [
    'about-us.html', 'buyer-rfqs.html', 'contact.html', 'create-rfq.html',
    'custom-payment.html', 'for-suppliers.html', 'how-to-export.html',
    'learn-exporting.html', 'privacy.html', 'refund-policy.html',
    'register-buyer.html', 'register-supplier.html', 'standards.html',
    'supplier-dashboard.html', 'supplier-login.html', 'suppliers.html',
    'terms.html', 'trust-and-safety.html'
]

for fname in pages_to_update:
    if os.path.exists(fname):
        with open(fname, 'r', encoding='utf-8') as f:
            content = f.read()
        if 'code.tidio.co' not in content:
            if '</body>' in content:
                new_content = content.replace('</body>', tidio_snippet + '\n</body>')
                with open(fname, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Injected Tidio into {fname}")
            else:
                print(f"No </body> tag in {fname}")
        else:
            print(f"Tidio already present in {fname}")
