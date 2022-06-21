pipeline {
    agent any
    triggers {
        pollSCM('* * * * *')
    }
    stages {
        stage("Unit Test") {
            steps {
                sh "python -m unittest test_calculator.py"
            }
        }
    }
}