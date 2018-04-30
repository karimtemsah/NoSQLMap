import sys
import getopt
import ast
import nsmweb

def check_args(args):
    """
        args[0]: http_method (get or post)
        args[1]: webPort (int)
        args[2]: victim (base link)
        args[3]: uri (path)
        args[4]: https (On for https, Off for http)
        args[5]: verbose (On or Off)
        args[6]: request_headers (dict), example: "{'referer':'http://example.com'}"
    """
    if args[0].lower() not in ['get', 'post']:
        print("HTTP method should be GET or POST")
        return False
    if not args[1].isdigit():
        print("Web port should be Integer")
        return False
    if len(args[3]) > 0 and args[3][0] != '/':
        args[3] = '/' + args[3]
    if args[4].lower() not in ['on', 'off']:
        print("HTTPS should be set to ON or OFF")
        return False
    if args[5].lower() not in ['on', 'off']:
        print("Verbose should be set to ON or OFF")
        return False
    args[6] = ast.literal_eval(args[6])
    if type(args[6]) is not dict:
        print("Request Headers should be dictionary like")
        return False
    return True


if __name__ == "__main__":
    opts, args = getopt.getopt(sys.argv[1:], "h", [
        "post-params=",
        "inject-size=",
        "inject-option=",
        "inject-parameters="
        "timing-attack=",
        "brute-force-attack=",
        "save-to-file=",
        "file-path=",
        "get-db-users="
    ])
    data = {}
    if not check_args(args):
        sys.exit(-1)
    for opt, arg in opts:
        if opt == '--post-params':
            data['post-params'] = ast.literal_eval(arg)
        if opt == '--inject-size':
            data['inject-size'] = arg
        if opt == '--inject-parameters':
            data['inject-parameters'] = arg
        if opt == '--inject-option':
            data['inject-option'] = arg
        if opt == '--timing-attack':
            data['timing-attack'] = arg
        if opt == '--brute-force-attack':
            data['brute-force-attack'] = arg
        if opt == '--save-to-file':
            data['save-to-file'] = arg
        if opt == '--file-path':
            data['file-path'] = arg
        if opt == '--get-db-users':
            data['get-db-users'] = arg

    if args[0].lower() == 'get':
        nsmweb.getApps(args[1], args[2], args[3], args[4], args[5], args[6], data)
    elif args[0].lower() == 'post':
        if 'post-params' not in data.keys():
            print 'No post parameters provided'
            sys.exit(-1)
        nsmweb.postApps(args[2], args[1], args[3], args[4], args[5], data['post-params'], args[6], data)


