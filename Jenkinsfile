pipeline {
    agent any
    triggers {
        pollSCM('* * * * *')
    }
    stages {
        stage("Unit Test") {
            steps {
                sh "python3 -m unittest test_calculator.py"
            }
        }
    }
}