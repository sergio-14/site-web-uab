document.addEventListener('DOMContentLoaded', function () {
    particlesJS(
        {
            "particles": {
                "number": {
                    "value": 100,
                    "density": {
                        "enable": true,
                        "value_area": 700
                    }
                },
                "color": {
                    "value": "#bbc7fa"
                },
                "shape": {
                    "type": "circle",
                    "stroke": {
                        "width": 2,
                        "color": "#b47413"
                    },
                    "polygon": {
                        "nb_sides": 5
                    },
                   
                },
                "opacity": {
                    "value": 0.5,
                    "random": false,
                    "anim": {
                        "enable": false,
                        "speed": 1,
                        "opacity_min": 0.1,
                        "sync": false
                    }
                },
                "size": {
                    "value": 3,
                    "random": true,
                    "anim": {
                        "enable": false,
                        "speed": 40,
                        "size_min": 0.1,
                        "sync": false
                    }
                },
                "line_linked": {
                    "enable": true,
                    "distance": 150,
                    "color": "#07485c",
                    "opacity": 0.6,
                    "width": 2
                },
                "move": {
                    "enable": true,
                    "speed": 4.22388442605866,
                    "direction": "none",
                    "random": false,
                    "straight": false,
                    "out_mode": "out",
                    "bounce": false,
                    "attract": {
                        "enable": false,
                        "rotateX": 600,
                        "rotateY": 1200
                    }
                }
            },
            "interactivity": {
                "detect_on": "canvas",
                "events": {
                    "onhover": {
                        "enable": true,
                        "mode": "repulse" // Cambia el modo a "repulse" para que las partículas se alejen al pasar el cursor
                    },
                    "onclick": {
                        "enable": true,
                        "mode": "push"
                    },
                    "resize": true
                },
                "modes": {
                    "repulse": { // Configuración específica para el modo "repulse"
                        "distance": 100, // Puedes ajustar esta distancia según tu preferencia
                        "duration": 0.4 // Puedes ajustar la duración de la animación
                    }
                }
            },
            "retina_detect": true
        }
    );
});
