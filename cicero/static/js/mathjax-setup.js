MathJax.Hub.Config({
    tex2jax: {
      skipTags: ['script', 'noscript', 'style', 'textarea', 'pre'],
      inlineMath: [['$','$'], ['\\(','\\)']],
      processEscapes: true
    },
    "TeX": {
      Macros: {AA : "{\\unicode{x212B}}"},
      extensions: ["autoload-all.js"]
    },
    "HTML-CSS": {
      scale: 90
    }
});

MathJax.Hub.Queue(function() {
    $(MathJax.Hub.getAllJax()).map(function(index, elem) {
        return(elem.SourceElement());
    }).parent().addClass('has-jax');
});

MathJax.Hub.Configured();
