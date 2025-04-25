pipeline {
    agent none
    environment {
        // 万无一失地确保用新 pip
        PATH = "/usr/local/bin:/usr/local/opt/python@3.11/bin:${env.PATH}"
    }
    parameters {
        choice(name: 'PY_VERS',
               choices: ['3.10', '3.11'],
               description: 'Python version matrix')
    }
    stages {
        stage('Matrix Test') {
            parallel {
                stage("py${params.PY_VERS}") {
                    agent { label "local"}
                    steps {
                        sh """
                            pyenv global ${params.PY_VERS}
                            python3 -m pip install --upgrade pip
                            pip3 install -r requirements.txt
                            pytest -q
                        """
                    }
                }
            }

        }
    }
}