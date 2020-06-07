pipeline{
	agent any
	stages{
	    stage('Instalación'){
			steps{
			    sh "ansible-playbook -i ./ jenkins ./ deployment.yml"
			}
		}
		stage('Verificación de código'){
			steps{
				sh "autopep8 -i *.py */*.py"
				sh "flake8 --exclude = *migrations*,*settings*"
			}
		}
		stage('Testing'){
			steps{
				sh "python manage.py test Trabajaor"
				sh "behave  features/*.feature"
				sh "coverage run --source = '.' --omit = *test*, *migrations*, *__init* manage.py"
				sh "coverage report"
				sh "coverage html"
			}
		}
		stage('Build'){
			steps{
				echo "Build"
			}
		}
		stage('Servidor de pre-producción'){
			steps{
				sh "ansible-playbook -i ./ pre_aws_ec2.yml ./ deployment.yml"	
			}
		}
		stage('Servidor de producción'){
			input{
			        message "Quieres hacer el despligue a producción?"
			        ok "Si"
			}
			steps{
				echo "ansible-playbook -i ./ deployment.yml"
			}
		}
	}
}
chuckNorris()
