def deploy_hadoop():
    print('Initiating Apache Hadoop...' + '\n' + '-' * 30)
    return


def deploy_spark():
    print('Initiating Apache Spark...' + '\n' + '-' * 30)
    return


def deploy_jupyter():
    print('Initiating Jupyter Notebook...' + '\n' + '-' * 30)
    return


def deploy_sonar():
    print('Initiating SonarQube and SonarScanner...' + '\n' + '-' * 30)
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
