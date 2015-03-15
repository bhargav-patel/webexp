angular.module('quiz', [])
	.controller('mainController', ['$scope','$http', function($scope,$http) {
		$http.post('/quiz/getquestion')
			.success(function(data){
				console.log(data);
				$scope.que = data;
				console.log($scope.que.image);
			});
	}]).run(run)
	.config(function($interpolateProvider) {
		$interpolateProvider.startSymbol('{$');
		$interpolateProvider.endSymbol('$}');
	});;
	
	run.$inject = ['$http'];
  
	function run($http) {
	  $http.defaults.xsrfHeaderName = 'X-CSRFToken';
	  $http.defaults.xsrfCookieName = 'csrftoken';
	};