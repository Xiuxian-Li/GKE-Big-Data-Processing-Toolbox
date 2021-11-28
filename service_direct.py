import webbrowser

def deploy_hadoop():
    print('Access Apache Hadoop at http://34.72.201.49:80' + '\n' + '-' * 30)
    webbrowser.open('http://34.72.201.49:80') 
    return


def deploy_spark():
    print('Access Apache Spark at http://107.178.210.200:80' + '\n' + '-' * 30)
    webbrowser.open('http://107.178.210.200:80') 
    return


def deploy_jupyter():
    print('Access Jupyter Notebook at http://34.135.195.24:80' + '\n' + '-' * 30)
    webbrowser.open('http://34.135.195.24:80') 
    return


def deploy_sonar():
    print('Access SonarQube at http://34.136.28.166:80' + '\n' + '-' * 30)
    webbrowser.open('http://34.136.28.166:80') 
    return


if __name__ == '__main__':

    pop_info = """
    Welcome to Big data Processing Application
    Please type the number that corresponds to which application you would like to run:
    1. Apache Hadoop
    2. Apache Spark
    3. Jupyter Notebook
    4. SonarQube and SonarScanner
    """
    print(pop_info)

    service_dict = {
        1: deploy_hadoop,
        2: deploy_spark,
        3: deploy_jupyter,
        4: deploy_sonar
    }

    while True:
        print('\nService option > ')
        service_index = input()
        service_dict[int(service_index)]()
        print('\nRequire more services? (Y/N)')
        if input().upper() == 'N':
            break
