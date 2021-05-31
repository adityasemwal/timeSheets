pipeline {
	parameters {
		string(name: 'Activity_ID', description: 'Please enter Activity ID eg T002,T006,..', defaultValue: 'T002,T006,T017,T007,multi')
		string(name: 'Month_Year', description: 'Please enter month and year without space', defaultValue: 'jan21')
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
					if (!"${params.Activity_ID}" || !"${params.Month_Year}") {
						currentBuild.result = 'FAILED'
						error('Missing Parameters')
					}
				}
			}
		}
		stage ('Checkout') {
			steps {
				git branch: 'master', credentialsId: 'adityasemwalGithub', poll: false, url: "https://github.com/adityasemwal/timeSheets.git"
			}
		}

		stage ('Check Sheet Hours') {
			steps {
				sh "./integrate.py ${params.Activity_ID} ${params.Month_Year}"
			
			}
		}
	}
}
