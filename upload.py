import json
import itertools
import requests
import time

from cryptography.hazmat.primitives.hashes import SHA256


def upload_file():
    upload_url = "http://api.pingstart.com/v3/sdk-api"
    '''
    data = {"pv": 1, "publisher_id": "5176", "from": 1, "timestamp": "1503385315",
            "imp": {"slot_id": "4", "ad_type": 1, "amount": 100},
            "app": {"id": "app_id_1", "name": "app_name", "ver": "1.1", "appkey": "app_key", "bundle": "com.bundle.cn",
                    "keywords": ""}, "device": {"geo": {"lat": 1.1, "lon": 1.2, "mcc": "us", "mnc": ""},
                                                "screen": {"dpi": 1, "w": 960, "h": 1440, "orientation": 1,
                                                           "density": 0}, "tzone": "Asha/shanghai",
                                                "idfa": "511F7987-6E2F-473A-BFED-E4C52CB5A6DC",
                                                "idfav": "511F7987-6E2F-473A-BFED-E4C52CB5A6DC", "limit": False,
                                                "aid": "aid", "gaid": "goole_id_goole_id", "carrier": "", "lang": "en",
                                                "brand": "apple", "model": "ios7,1", "sdkv": "1.1", "gp": 0, "pf": 2,
                                                "osv": "ios", "ispcode": "isp", "nt": 2, "Ijb": 0, "user_id": "1111",
                                                "udid": "udid"}, "bcat": [], "badv": []}
    #print(json.dumps(data))
    #s = requests.session()
    '''
    config_result = config_set()
    for data in config_result:
        try:
            req = requests.post(upload_url,data=json.dumps(data), timeout=20)
        except Exception as e:
            print(e,data)
        ads_result = json.loads(req.content)
        try:
            for i in range(len(ads_result['ads'])):
                vvurl = ads_result['ads'][i]['video']['vvurl']
                iturl = ads_result['ads'][i]['video']['iturl']
                cturl = ads_result['ads'][i]['video']['cturl']
                print(len(cturl))
                for url_vvurl in vvurl:
                    s = requests.session()
                    req_url_vvurl = s.get(url_vvurl)
                    req_result = req_url_vvurl.content
                    req_result_de = req_result.decode(encoding='utf-8')
                    print('req_result:', req_result_de)
                    if req_result_de == 'success':
                        print('qqqqq')
                for url_iturl in iturl:
                    s = requests.session()
                    req_url_iturl = s.get(url_iturl)
                    iturl_result = req_url_iturl.content
                    req_iturlresult_de = iturl_result.decode(encoding='utf-8')
                    print('req_iturlresult:', req_iturlresult_de)
                    if req_iturlresult_de == 'success':
                        print('ppp')
                for url_cturl in cturl:
                    s = requests.session()
                    req_url_cturl = s.get(url_cturl)
                    req_cturlresult = req_url_cturl.content
                    req_cturlresult_de = req_cturlresult.decode(encoding='utf-8')
                    print('req_cturlresult:', req_cturlresult_de)
                    if req_cturlresult_de == 'success':
                        print('ccc')
            try:
                test = ads_result['ads'][i]['video']['vvurl']
            except Exception as e:
                print(data)
        except:
            print(ads_result,'---------------------------------------------------\n',data)





def config_set():
    pv = [1]     #协议版本
    publisher_id = ["5176"]  #媒体id
    from_0 = [1]  #1:onlie,2:offline
    timestamp =[str(time.time())] #unix时间戳
    bcat = [[]]
    badv = [[]]


#imp:
    slot_id = ["6"] #广告位
    ad_type = [0]  #1.video 2.native
    amount = [3]   #请求广告数量

    imp_list_result = []
    for i in range(len(slot_id)):
        for o in range(len(ad_type)):
            for p in range(len(amount)):
                imp_dict_result = {}
                imp_dict_result["slot_id"] = slot_id[i]
                imp_dict_result["ad_type"] = ad_type[o]
                imp_dict_result["amount"] = amount[p]

                imp_list_result.append(imp_dict_result)

    #print(type(slot_id[i]),imp_list_result)
    imp = imp_list_result


#app
    id = ["1"]  #app_id
    name = ["PingStartSample"] #app name
    ver = ["1.0","10004"] #app version
    appkey = ["app_key"] #bundleid or appkey
    bundle = ["com.testtttt.test","com.pingstart.sample"] #bundleid or appkey
    keywords = [""] #keyword

    app_list_result = []
    for a in range(len(id)):
        for b in range(len(name)):
            for c in range(len(ver)):
                for d in range(len(appkey)):
                    for e in range(len(bundle)):
                        for f in range(len(keywords)):
                            app_dict_result = {}
                            app_dict_result["id"] = id[a]
                            app_dict_result["name"] = name[b]
                            app_dict_result["ver"] = ver[c]
                            app_dict_result["appkey"] = appkey[d]
                            app_dict_result["bundle"] = bundle[e]
                            app_dict_result["keywords"] = keywords[f]

                            app_list_result.append(app_dict_result)
    app = app_list_result

#device{geo}
    lat = [0]
    lon = [0]
    mcc = [""]
    mnc = [""]
    carrier = ["ALE-TL00"]

    geo_list_result = []
    for geo_a in range(len(lat)):
        for geo_b in range(len(lon)):
            for geo_c in range(len(mcc)):
                for geo_d in range(len(mnc)):
                    for geo_e in range(len(carrier)):
                        geo_dict_result = {}
                        geo_dict_result["lat"] = lat[geo_a]
                        geo_dict_result["lon"] = lon[geo_b]
                        geo_dict_result["mcc"] = mcc[geo_c]
                        geo_dict_result["mnc"] = mnc[geo_d]
                        geo_dict_result["carrier"] = carrier[geo_e]

                        geo_list_result.append(geo_dict_result)


    geo = geo_list_result
    #print("22222", geo_list_result,len(geo))

#device{screen}
    dpi = [1,2]
    w = [375,720]
    h = [667,1208]
    orientation = [2,1]
    density = [0]

    screen_list_result = []
    for screen_a in range(len(dpi)):
        for screen_b in range(len(w)):
            for screen_c in range(len(h)):
                for screen_d in range(len(orientation)):
                    for screen_e in range(len(density)):
                        screen_dict_result = {}
                        screen_dict_result["dpi"] = dpi[screen_a]
                        screen_dict_result["w"] = w[screen_b]
                        screen_dict_result["h"] = h[screen_c]
                        screen_dict_result["orientation"] = orientation[screen_d]
                        screen_dict_result["density"] = density[screen_e]
                        #device_screen["screen"] = screen_dict_result
                        screen_list_result.append(screen_dict_result)

    screen = screen_list_result

    tzone = ["GMT+08:00"]
    idfa = ["511F7987-6E2F-473A-BFED-E4C52CB5A6DC"]
    idfv = ["21A8AB3A-8C76-4076-856F-F689352CC635"]
    limit = [True,False]
    aid = ["ccc9970b99d8aa9a"]
    gaid = ["005653ea-7f2e-4512-b2f1-f528bccd4810"]
    lang = ["zh"]
    brand = ["apple","Huawei"]
    model = ["iPhone7,2","ALE-TL00"]
    sdkv = ["1.1.0","3.6.0"]
    gp = [0,1]
    pf = [1,0]
    osv = ["10.2.1","23","6.0"]
    ispcode = ["isp"]
    nt = [0,1,2,3,4]
    Ijb = [0,1]
    user_id = [""]
    udid = ["1BD123AF-6972-40D9-89A4-1A0B679D80EC"]

    device_list_result = []
    for device_a in range(len(geo)):
        for device_b in range(len(screen)):
            for device_c in range(len(tzone)):
                for device_d in range(len(idfa)):
                    for device_e in range(len(idfv)):
                        for device_f in range(len(limit)):
                            for device_h in range(len(aid)):
                                for device_i in range(len(gaid)):
                                    for device_j in range(len(brand)):
                                        for device_k in range(len(model)):
                                            for device_l in range(len(lang)):
                                                for device_m in range(len(sdkv)):
                                                    for device_n in range(len(gp)):
                                                        for device_o in range(len(pf)):
                                                            for device_p in range(len(osv)):
                                                                for device_q in range(len(ispcode)):
                                                                    for device_r in range(len(nt)):
                                                                        for device_s in range(len(Ijb)):
                                                                            for device_t in range(len(user_id)):
                                                                                for device_u in range(len(udid)):
                                                                                    device_dict_result = {}
                                                                                    device_dict_result["geo"] = geo[
                                                                                        device_a]
                                                                                    device_dict_result["screen"] = \
                                                                                    screen[device_b]
                                                                                    device_dict_result["tzone"] = tzone[
                                                                                        device_c]
                                                                                    device_dict_result["idfa"] = idfa[
                                                                                        device_d]
                                                                                    device_dict_result["idfv"] = idfv[
                                                                                        device_e]
                                                                                    device_dict_result["limit"] = limit[
                                                                                        device_f]
                                                                                    device_dict_result["aid"] = aid[
                                                                                        device_h]
                                                                                    device_dict_result["gaid"] = gaid[
                                                                                        device_i]
                                                                                    device_dict_result["brand"] = brand[
                                                                                        device_j]
                                                                                    device_dict_result["model"] = model[
                                                                                        device_k]
                                                                                    device_dict_result["lang"] = lang[
                                                                                        device_l]
                                                                                    device_dict_result["sdkv"] = sdkv[
                                                                                        device_m]
                                                                                    device_dict_result["gp"] = gp[
                                                                                        device_n]
                                                                                    device_dict_result["pf"] = pf[
                                                                                        device_o]
                                                                                    device_dict_result["osv"] = osv[
                                                                                        device_p]
                                                                                    device_dict_result["ispcode"] = \
                                                                                    ispcode[device_q]
                                                                                    device_dict_result["nt"] = nt[
                                                                                        device_r]
                                                                                    device_dict_result["Ijb"] = Ijb[
                                                                                        device_s]
                                                                                    device_dict_result["user_id"] = \
                                                                                    user_id[device_t]
                                                                                    device_dict_result["udid"] = udid[
                                                                                        device_u]
                                                                                    #device["device"] = device_dict_result
                                                                                    #print(device["device"])
                                                                                    device_list_result.append(device_dict_result)
    #print(device_list_result,len(device_list_result))
    device = device_list_result
    #print(device)

    config_list_result = []
    for config_a in range(len(pv)):
        for config_b in range(len(publisher_id)):
            for config_c in range(len(from_0)):
                for config_d in range(len(timestamp)):
                    for config_e in range(len(imp)):
                        for config_f in range(len(app)):
                            for config_h in range(len(device)):
                                for config_i in range(len(bcat)):
                                    for config_j in range(len(badv)):
                                        config_dict_result = {}
                                        config_dict_result["pv"] = pv[config_a]
                                        config_dict_result["publisher_id"] = publisher_id[config_b]
                                        config_dict_result["from"] = from_0[config_c]
                                        config_dict_result["timestamp"] = timestamp[config_d]
                                        config_dict_result["imp"] = imp[config_e]
                                        config_dict_result["app"] = app[config_f]
                                        config_dict_result["device"] = device[config_h]
                                        config_dict_result["bcat"] = bcat[config_i]
                                        config_dict_result["badv"] = badv[config_j]
                                        # device_screen["screen"] = config_dict_result
                                        config_list_result.append(config_dict_result)
    config = config_list_result
    print(json.dumps(config[0]))
    return  config






upload_file()
"""

        "device": {
            "ispcode": "isp",
            "nt": 2,
            "Ijb": 0,
            "user_id": "1111",
            "udid": "udid"
        },
        "bcat": [

        ],
        "badv": [

        ]
    }
"""


