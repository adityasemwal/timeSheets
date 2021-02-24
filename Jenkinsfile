pipeline {
	parameters {
		string(name: 'ActivityCodes', description: 'Please enter Activity Codes eg["T002","T003"..]')
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

		stage ('Check Sheet Hours') {
			steps {
					sh "integrate.py ${params.ActivityCodes}"
				
			}
		}
	}
}
