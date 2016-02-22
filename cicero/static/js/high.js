

/*
Language: remark markdown flavor
Author: Ole Petter Bang <olepbang@gmail.com>
*/
hljs.registerLanguage('remark', function () {
  return {
    contains: [
      {
        className: 'keyword',
        begin: '^#+[^\n]+',
        relevance: 10
      },
      {
        className: 'comment',
        begin: '^---?'
      },
      {
        className: 'string',
        begin: '^\\w+:'
      },
      {
        className: 'literal',
        begin: '\\{\\{', end: '\\}\\}'
      }
    ]
  };
});


hljs.registerLanguage('shell', function () {
  return {
    contains: [
      {
        className: 'keyword',
        begin: '\\$+[^\n#]+',
      },
      {
        className: 'comment',
        begin: '#+[^\n]+',
      },
      {
        className: 'comment',
        begin: '#',
      },
      {
        className: 'literal',
        begin: '\\{\\{', end: '\\}\\}'
      }
    ]
  };
});
