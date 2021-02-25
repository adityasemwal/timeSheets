pipeline {
	parameters {
		string(name: 'ActivityCodes', description: 'Please enter Activity Codes eg T002,T006,..', defaultValue: 'T002,T006,T017,T007,multi')
	}

	options {
		//ansiColor('xterm')
		//skipDefaultCheckout()
		timestamps()
	}

	agent any


	stages {
		stage ('Validation') {
			steps {
				script {
					if (!"${params.ActivityCodes}" ) {
						currentBuild.result = 'FAILED'
						error('Missing Parameters')
					}
				}
			}
		}
//		stage ('Checkout') {
//			steps {
//				git branch: 'master', poll: false, url: "https://github.com/adityasemwal/timeSheets.git"
//			}
//		}

		stage ('Check Sheet Hours') {
			steps {
					sh "./integrate.py ${params.ActivityCodes}"
			
			}
		}
	}
}
