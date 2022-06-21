pipeline {
    agents any
    stages {
        stage("Unit Test") {
            steps {
                sh "python -m unittest test_calculator.py"
            }
        }
    }
}