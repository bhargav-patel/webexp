angular.module('quiz', [])
	.controller('mainController', ['$scope','$http', function($scope,$http) {
		$scope.getQuestion = function(){
			$http.post('/quiz/getquestion')
				.success(function(data){
					console.log(data);
					$scope.que = data;
					console.log($scope.que.image);
				});
		}
		$scope.checkAnswer = function(){
			$http.post('/quiz/checkanswer',{level:$scope.que.level,answer:$scope.answer})
				.success(function(data){
					if(data.status=="true")
					{
						$scope.answer="";
						$scope.getQuestion();
					}
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