angular.module('quiz', [])
	.controller('mainController', ['$scope','$http', function($scope,$http) {
		var options =  {
			content: 'initial',
			style: "snackbar",
			timeout: 2000 ,
			htmlAllowed: true 
		}
		function showSB(text,type){
			options.content='<div class="panel panel-'+type+'"><div class="panel-heading"><h3 class="panel-title">'+text+'</h3></div></div>'
			$.snackbar(options);
		}
		$scope.setLifeline = function(type){
			$scope.llType = type;
			if(type==1)
				$scope.llDesc = 'This will skip this question.';
			else if(type==2)
				$scope.llDesc = 'This will give you hint.';
			else
				$scope.llDesc = 'This will give you link of page. You will find answer on that link.';
		}
		$scope.useLifeline = function(){
			$scope.loading = true;
			$http.post('/quiz/uselifeline',{"level":$scope.que.level,"type":$scope.llType})
				.success(function(data){
					if(data.status=="success")
					{
						showSB('Lifeline Unlocked.','success');
						if(data.type==1)
						{
							$scope.getQuestion();
						}
						else if(data.type==2)
						{
							$scope.llHint = data.hint;
						}
						else if(data.type==3)
						{
							$scope.llLink = data.link;
						}
					}
					else if(data.status=="fail")
					{
						showSB('Already Used.','warning');
					}
					else
					{
						showSB('Error : Contact Coordinatior.','danger');
					}
					$scope.loading = false;
				});
		}
		$scope.getQuestion = function(){
			$scope.loading = true;
			$http.post('/quiz/getquestion')
				.success(function(data){
					$scope.que = data;
					$scope.llHint="";
					$scope.llLink="";
					$scope.lbUpdate();
					$scope.loading = false;
				});
		}
		$scope.checkAnswer = function(){
			$scope.loading = true;
			$http.post('/quiz/checkanswer',{"level":$scope.que.level,"answer":$scope.answer})
				.success(function(data){
					if(data.status=="true")
					{
						$scope.answer="";
						showSB('GoodJob','success');
						$scope.getQuestion();
					}
					else if(data.status=="false")
					{
						showSB('Wrong Answer. Try Again.','warning');
					}
					else
					{
						showSB('Error : Contact Coordinatior.','danger');
					}
					$scope.loading = false;
				});
		}
		$scope.lbUpdate = function(){
			$scope.loading = true;
			$http.post('/quiz/gettop')
				.success(function(data){
					$scope.lbData = data;
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