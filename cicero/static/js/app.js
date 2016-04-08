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

    $scope.user = '';

    $scope.repo = '';
    $scope.repos = [];
    $scope.show_repos = false;
    $scope.load_repos = function () {
        $scope.show_repos = false;
        $scope.show_branches = false;
        $scope.show_files = false;

        $http.get("https://api.github.com/users/" + $scope.user + "/repos?per_page=1000")
            .success(function(data) {
                $scope.repos = data;
                $scope.show_repos = true;
            })
    };

    $scope.branch = '';
    $scope.branches = [];
    $scope.show_branches = false;
    $scope.load_branches = function () {
        $scope.show_branches = false;
        $scope.show_files = false;

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

    $scope.file = '';
    $scope.files = [];
    $scope.show_files = false;
    $scope.load_files = function () {
        $scope.show_files = false;

        $http.get("https://api.github.com/repos/" + $scope.user + "/" + $scope.repo.name + "/git/refs/heads/" + $scope.branch.name)
            .success(function(data) {
            $http.get("https://api.github.com/repos/" + $scope.user + "/" + $scope.repo.name + "/git/trees/" + data.object.sha + "?recursive=1")
                .success(function(data2) {
                    $scope.files = [];
                    var _files = data2.tree;
                    for (var i = 0; i < _files.length; i++) {
                        if (_files[i].path.endsWith('.md') || _files[i].path.endsWith('.mkd'))
                        {
                            $scope.files.push(_files[i]);
                        }
                    }
                    $scope.show_files = true;
                })
            })
    };

    $scope.link = '';
    $scope.source_link = '';
    $scope.link_generated = false;
    $scope.generate_link = function () {

        $scope.link = 'http://cicero.xyz/v2/remark/github/'
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

        $scope.link_generated = true;
    };

}]);


// close the anonymous function
})();
