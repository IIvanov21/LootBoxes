pipeline{
        agent any
        environment{
            DATABASE_URI= credentials("DATABASE_URI")
            DOCKER_ID=credentials("DockerID")
        }
        stages{
            stage('Setup'){
                steps{
                    
                }
            }
            stage('Test'){
                steps{
                }
            }
            stage('Build'){
                steps{
                    sh "bash ./scripts/build.sh"
                }
            }
            stage('Config'){
                steps{
                }
            }
            stage('Deploy'){
                steps{
                }
            }
        }
}