
import jpush

__jpush = jpush.JPush('ba930456252a3ac98c746dc7', 'b5ae4b7a4ff60e5c9045b278')


push = __jpush.create_push()


__jpush.set_logging("DEBUG")


push.audience = jpush.all_


push.notification = jpush.notification(alert="hello python jpush api")


push.platform = jpush.all_


try:
    response=push.send()
except common.Unauthorized:
    raise common.Unauthorized("Unauthorized")
except common.APIConnectionException:
    raise common.APIConnectionException("conn error")
except common.JPushFailure:
    print ("JPushFailure")
except:
    print ("Exception")