pipeline{
	agent any
	stages{
	    stage('Instalación'){
			steps{
			    echo "sudo apt-get update"
				echo "sudo apt-get install python3 python3-pip"
				echo "sudo pip install virtualenv"
				echo "virtualenv entorno"
				echo "source entorno/bin/activate"
				echo "pip install -r requirements.txt"
			}
		}
		stage('Verificación de código'){
			steps{
				echo "autopep8 -i *.py */*.py"
				echo "flake8 --exclude = *migrations*,*settings*"
			}
		}
		stage('Testing'){
			steps{
				echo "python manage.py test Trabajaor"
				echo "behave  features/*.feature"
				echo "coverage run --source = '.' --omit = *test*, *migrations*, *__init* manage.py"
				echo "coverage report"
				echo "coverage html"
			}
		}
		stage('Build'){
			steps{
				echo "jar cvf SCATUAZ.war"
				echo "sudo cp -r /home/vagrant/SCATUAZ/SCATUAZ.war /var/lib/tomcat8/webapps/SCATUAZ.war"
				echo "systemctl reload tomcat8"
			}
		}
		stage('Servidor de pre-producción'){
			steps{
				echo "sudo a2ensite configuracion.conf"
				echo "systemctl reload apache2"
			}
		}
		stage('Servidor de producción'){
			input{
			        message "Quieres hacer el despligue a producción?"
			        ok "Si"
			}
			steps{
				echo "sudo a2ensite configuracion.conf"
				echo "systemctl reload apache2"

			}
		}
	}
}
chuckNorris()
