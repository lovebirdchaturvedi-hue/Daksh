import * as THREE from 'https://cdn.skypack.dev/three@0.132.2';

class TradeGlobe {
    constructor(containerId) {
        this.container = document.getElementById(containerId);
        if (!this.container) return;

        this.scene = new THREE.Scene();
        this.camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);
        this.renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
        
        this.renderer.setSize(window.innerWidth, window.innerHeight);
        this.renderer.setPixelRatio(window.devicePixelRatio);
        this.container.appendChild(this.renderer.domElement);

        this.globe = null;
        this.arcs = [];
        this.mouse = { x: 0, y: 0 };
        this.targetRotation = { x: 0, y: 0 };

        this.init();
    }

    init() {
        // Lights
        const ambientLight = new THREE.AmbientLight(0xffffff, 0.6);
        this.scene.add(ambientLight);

        const spotLight = new THREE.SpotLight(0xc9a44a, 2);
        spotLight.position.set(10, 10, 10);
        this.scene.add(spotLight);

        // 1. The Core Sphere (Digital Grid)
        const geometry = new THREE.SphereGeometry(2, 64, 64);
        const material = new THREE.PointsMaterial({
            color: 0xc9a44a,
            size: 0.045, 
            transparent: true,
            opacity: 0.8
        });
        
        this.globe = new THREE.Points(geometry, material);
        this.scene.add(this.globe);

        // 2. THE "LUCRATIVE" ADDITIONS: Golden Rings
        this.rings = [];
        for(let i = 0; i < 3; i++) {
            const ringGeo = new THREE.RingGeometry(2.4 + (i * 0.1), 2.42 + (i * 0.1), 128);
            const ringMat = new THREE.MeshBasicMaterial({ 
                color: 0xc9a44a, 
                side: THREE.BackSide, 
                transparent: true, 
                opacity: 0.2 - (i * 0.05) 
            });
            const ring = new THREE.Mesh(ringGeo, ringMat);
            ring.rotation.x = Math.PI / 2 + (Math.random() * 0.5);
            this.scene.add(ring);
            this.rings.push(ring);
        }

        // 3. Glowing Atmosphere (Aura)
        const auraGeo = new THREE.SphereGeometry(2.1, 64, 64);
        const auraMat = new THREE.MeshBasicMaterial({
            color: 0xc9a44a,
            transparent: true,
            opacity: 0.05,
            side: THREE.BackSide
        });
        const aura = new THREE.Mesh(auraGeo, auraMat);
        this.scene.add(aura);

        // Trade Arcs from India (approx coords)
        this.addTradeArc({ lat: 20, lon: 78 }, { lat: 40, lon: -74 }); // India -> USA
        this.addTradeArc({ lat: 20, lon: 78 }, { lat: 25, lon: 55 });  // India -> Dubai
        this.addTradeArc({ lat: 20, lon: 78 }, { lat: 1, lon: 103 });  // India -> Singapore
        this.addTradeArc({ lat: 20, lon: 78 }, { lat: 51, lon: 0 });   // India -> London

        this.camera.position.z = 6;

        this.animate();
        this.handleResize();
        this.handleMouse();
    }

    addTradeArc(start, end) {
        const startPos = this.latLonToVector3(start.lat, start.lon, 2);
        const endPos = this.latLonToVector3(end.lat, end.lon, 2);
        
        const midX = (startPos.x + endPos.x) / 2;
        const midY = (startPos.y + endPos.y) / 2;
        const midZ = (startPos.z + endPos.z) / 2;
        
        const midPos = new THREE.Vector3(midX, midY, midZ).multiplyScalar(1.5); // Elevation

        const curve = new THREE.QuadraticBezierCurve3(startPos, midPos, endPos);
        const points = curve.getPoints(50);
        const geometry = new THREE.BufferGeometry().setFromPoints(points);
        const material = new THREE.LineBasicMaterial({ color: 0xe7cf88, transparent: true, opacity: 0.3 });
        
        const line = new THREE.Line(geometry, material);
        line.renderOrder = 1; // Ensure arcs are always on top
        this.globe.add(line);
    }

    latLonToVector3(lat, lon, radius) {
        const phi = (90 - lat) * (Math.PI / 180);
        const theta = (lon + 180) * (Math.PI / 180);

        return new THREE.Vector3(
            -radius * Math.sin(phi) * Math.cos(theta),
            radius * Math.cos(phi),
            radius * Math.sin(phi) * Math.sin(theta)
        );
    }

    handleMouse() {
        document.addEventListener('mousemove', (e) => {
            this.mouse.x = (e.clientX / window.innerWidth) - 0.5;
            this.mouse.y = (e.clientY / window.innerHeight) - 0.5;
        });
    }

    handleResize() {
        window.addEventListener('resize', () => {
            this.camera.aspect = window.innerWidth / window.innerHeight;
            this.camera.updateProjectionMatrix();
            this.renderer.setSize(window.innerWidth, window.innerHeight);
        });
    }

    animate() {
        requestAnimationFrame(this.animate.bind(this));

        // Subtle Globe rotation
        this.globe.rotation.y += 0.0015;

        // 4. Animate Rings (Lucrative Motion)
        if (this.rings) {
            this.rings.forEach((ring, idx) => {
                ring.rotation.z += 0.002 * (idx + 1);
            });
        }

        // Mouse parallax
        this.targetRotation.x += (this.mouse.y * 0.3 - this.targetRotation.x) * 0.05;
        this.targetRotation.y += (this.mouse.x * 0.3 - this.targetRotation.y) * 0.05;
        
        this.globe.rotation.x = this.targetRotation.x;
        this.globe.rotation.y += this.targetRotation.y;

        this.renderer.render(this.scene, this.camera);
    }
}

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    new TradeGlobe('globe-container');
});
