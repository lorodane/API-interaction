from restb.examples import basic, multipredict, rate_limiting_simple, rate_limiting_robust, value


if __name__ == '__main__':
    client_key = '668e94100dc9e3598afe9294abac3379e73e3c306c8d9e1b29dbce0ad505a90a'
    print('1. running modified basic example')
    value.run(client_key)
    # print('2. running multipredict example')
    # multipredict.run(client_key)
    # print('3. running simple rate limiting example')
    # rate_limiting_simple.run(client_key)
    # print('4. running robust rate limiting example')
    # rate_limiting_robust.run(client_key)
