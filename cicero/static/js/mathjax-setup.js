MathJax.Hub.Config({
    tex2jax: {
    skipTags: ['script', 'noscript', 'style', 'textarea', 'pre']
    }
});
MathJax.Hub.Queue(function() {
    $(MathJax.Hub.getAllJax()).map(function(index, elem) {
        return(elem.SourceElement());
    }).parent().addClass('has-jax');
});

MathJax.Hub.Configured();
