from controller.config_controller import load_config, save_config
import services.auth_service as AuthService

def register(username, password):
    """
    Handle the sign-up process. UI should auto login after sign up succeed. Write data into config.json
    :param username:
    :param password:
    :return:
    """

    response = AuthService.register(username, password)
    # print(f'[FRONTEND DEBUG] Response: \n{response}')
    # print(f"[DEBUG] AuthService.register response: {response}")
    if response.get('status') == 'success':
        config = load_config()
        print(f'[FRONTEND DEBUG] UID: {response.get('uid')}')
        config['uid'] = response.get('uid')
        config['username'] = username
        config['password'] = password
        save_config(config)
        return True, "注册成功，自动登录"
    else:
        return False, response.get('message', '注册失败')

def login(username, password):
    """
    Handle the login process. Write data into config.json
    :param username:
    :param password:
    :return:
    """

    response = AuthService.login(username, password)
    # print(f'[FRONTEND DEBUG] Response: \n{response}')
    if response.get('status') == 'success':
        config = load_config()
        print(f'[FRONTEND DEBUG] UID: {response.get('uid')}')
        config['uid'] = response.get('uid')
        config['username'] = username
        config['password'] = password
        save_config(config)
        return True, "登陆成功"
    else:
        return False, response.get('message', '登录失败')

def logout():
    """
    Handle the log-out process.
    :return:
    """

    try:
        config = load_config()
        config.pop('uid', None)
        config.pop('username', None)
        config.pop('password', None)
        save_config(config)
        return True, "已登出"
    except Exception as exception:
        return False, f"登出失败，错误：{exception}"

def edit_user(username, old_password, new_password):
    """
    Handle the modification of user password and data
    :param username:
    :param old_password:
    :param new_password:
    :return:
    """

    response = AuthService.edit_user(username, old_password, new_password)
    if response.get('status') == 'success':
        config = load_config()
        config['username'] = username
        config['password'] = new_password
        save_config(config)
        return True, "修改成功"
    else:
        return False, response.get('message', '修改失败')