#Print Hello World 10 Times in Python, Bash and Powershell
#Python
for i in range(10):
    print("Hello World!")

#Bash
for i in {1..10}; do
    echo Hello World!

#Powershell
for ($1; $i -le 10; $i++) {
    Write-Host "Hello World!"
}