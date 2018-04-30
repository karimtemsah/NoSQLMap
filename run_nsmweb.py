import sys
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
        args[7]: post_data (dict)
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
    args = sys.argv[1:]
    if not check_args(args):
        sys.exit(-1)

    if args[0].lower() == 'get':
        nsmweb.getApps(args[1], args[2], args[3], args[4], args[5], args[6])
    elif args[0].lower() == 'post':
        nsmweb.postApps(args[2], args[1], args[3], args[4], args[5], args[7], args[6])


