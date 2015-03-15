angular.module('quiz', [])
	.controller('mainController', ['$scope','$http', function($scope,$http) {
		$scope.getQuestion = function(){
			$scope.loading = true;
			$http.post('/quiz/getquestion')
				.success(function(data){
					$scope.que = data;
					$scope.loading = false;
				});
		}
		$scope.checkAnswer = function(){
			$scope.loading = true;
			$http.post('/quiz/checkanswer',{level:$scope.que.level,answer:$scope.answer})
				.success(function(data){
					if(data.status=="true")
					{
						$scope.answer="";
						$scope.getQuestion();
					}
					$scope.loading = false;
				});
		}
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