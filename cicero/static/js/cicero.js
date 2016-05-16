// we put all the js code into an anonymous function
// this is good practice to isolate the namespace
; (function() {


// with this we make js less forgiving so that we catch
// more hidden errors during development
'use strict';


var app = angular.module('app', []);


app.config(['$interpolateProvider', function($interpolateProvider) {
    $interpolateProvider.startSymbol('{[');
    $interpolateProvider.endSymbol(']}');
}]);


app.controller('Ctrl', ['$scope', '$http', function($scope, $http) {


    function reset_links()
    {
        $scope.link = '';
        $scope.source_link = '';
        $scope.show_links = false;
    }


    function reset_files()
    {
        $scope.file = '';
        $scope.files = [];
        $scope.show_files = false;
        $scope.no_files_found = false;
        reset_links();
    }


    function reset_branches()
    {
        $scope.branch = '';
        $scope.branches = [];
        $scope.show_branches = false;
        reset_files();
    }


    function reset_repos()
    {
        $scope.repo = '';
        $scope.repos = [];
        $scope.show_repos = false;
        reset_branches();
    }


    $scope.user = '';
    reset_repos();


    $scope.load_repos = function () {
        reset_repos();
        $http.get("https://api.github.com/users/" + $scope.user + "/repos?per_page=1000")
            .success(function(data) {
                $scope.repos = data;
                $scope.show_repos = true;
            })
    };


    $scope.load_branches = function () {
        reset_branches();
        $http.get("https://api.github.com/repos/" + $scope.user + "/" + $scope.repo.name + "/branches")
            .success(function(data) {
                $scope.branches = data;

                // if there is only one branch, then we don't force the user to select it
                // and instead we jump right to file selector
                if ($scope.branches.length == 1)
                {
                    $scope.branch = $scope.branches[0];
                    $scope.load_files();
                }
                else
                {
                    $scope.show_branches = true;
                }
            })
    };


    $scope.load_files = function () {
        reset_files();
        $http.get("https://api.github.com/repos/" + $scope.user + "/" + $scope.repo.name + "/git/refs/heads/" + $scope.branch.name)
            .success(function(data) {
            $http.get("https://api.github.com/repos/" + $scope.user + "/" + $scope.repo.name + "/git/trees/" + data.object.sha + "?recursive=1")
                .success(function(data2) {
                    $scope.files = [];
                    var _files = data2.tree;
                    var num_markdown_files = 0;
                    for (var i = 0; i < _files.length; i++) {
                        if (_files[i].path.endsWith('.md') || _files[i].path.endsWith('.mkd'))
                        {
                            $scope.files.push(_files[i]);
                            num_markdown_files += 1;
                        }
                    }
                    if (num_markdown_files < 1)
                    {
                        $scope.no_files_found = true;
                    }
                    else
                    {
                        $scope.show_files = true;
                    }
                })
            })
    };


    $scope.generate_link = function () {
        $scope.link = '/v2/remark/github/'
                    + $scope.user
                    + '/'
                    + $scope.repo.name
                    + '/'
                    + $scope.branch.name
                    + '/'
                    + $scope.file.path
                    + '/';

        $scope.source_link = 'https://github.com/'
                           + $scope.user
                           + '/'
                           + $scope.repo.name
                           + '/blob/'
                           + $scope.branch.name
                           + '/'
                           + $scope.file.path;

        $scope.show_links = true;
    };

}]);


// close the anonymous function
})();
