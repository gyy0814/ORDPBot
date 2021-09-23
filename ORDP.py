import datetime
import pymysql
import time

DDZY_Str = '''《ORDP群调度指引》
为了确保ORDP群游戏跑车主题顺利实施，对调度员（以下简称行调）角色做如下普适性说明，由ORDP群服发布，为行调操作指引并事故处罚参考依据，内容如下：
1、 行调是一场联控的核心，需要担负游戏指挥，玩家协调，场面控制，玩法引导，陪带新人的任务。行调应维护连控游戏秩序，不组织，不纵容过度的 瞎搞或刷分行为。
2、 任何司机将在游戏内以行调为中心，听从并执行行调的任何调度指令，行调对所下指令的有效执行结果负全责。
3、 行调力求达到线路最大通过率，平衡玩家游戏驾驶与等待时间，全部调令下达均以列车行驶条件为参考，尽量避免多余的停车等待。
4、 行调需要公布游戏端口，游戏线路，预期调度时间，提供玩家进游戏的问题解答，但不包括提供编组文件和路径文件。
5、行调应用游戏内手段解决游戏内遇到问题，不轻易使用踢人踢车权限。遇到故意捣乱端口者除外。
6、行调不得以任何理由拒绝正常跑车玩家进入端口，并采取拖延，无视等手段压制正常进游戏玩家。
7、对于不确定的编组或车次行调应以最保守的车次和限速给于安排，并给出最稳妥的调度命令，并在游戏结束后自行补充相关知识。
8，行调要有巡线的习惯，线路情况应该主动发现，司机上报路况只能作为辅助，不能将司机看道作为替代巡线的方法。
9、出现事故时，行调应尊重游戏现状，游戏内的事故游戏内解决，不建议用踢人踢车的方式来清理堵塞，除非明确是无法通过调度解决的卡端事故。
10、任何形式联控时，行调都应该指令明确，发布及时，语音指令确认司机收到，文字指令确认记录在案。
11、行调安排行车应考虑兼顾玩家进端口先后顺序，玩家驾驶水平稳定性，列车编组与车站适配度，合理利用停站错位解决避让，不唯一根据车次限速安排行车。
12，行调有考察司机技术的权利，在一定时间内行调可以用适当手段测试司机驾驶技术和游戏进退习惯，以减少无畏的避让，优先照顾跑图车。
13，行调不能做无理由的停车安排，需保证在线路可以运行的情况下尽快发出车辆，照顾力度为：正线列车>停站列车>调车机车
14，行调应避免下达冒险的调度命令，不要刻意安排停车营造场景摆拍，背离跑图调度角度，误入观景截图角色。
15、当场行调不能继续调度时，提前做好调度接替预告，如遇新调度交接对于遗留操作要及时交接。严禁在不通知的情况下放弃调度角色。
16，行调应及时恢复使用后的道岔，保证正线默认开通，注意列车尾部道岔防护。管控好关键位置分向道岔，避免列车误开进路又安排退行。
17，行调应严格管理出站信号机，手动确认出站信号颜色，严格管理进站信号机，保证给出正确停车引导，尽量减少干预区间信号机，利用游戏自动闭塞功能。使游戏信号计算最小被干预。
18、行调接车应考虑站台接车能力，避免接车后股道无法容纳，列车过标情况调度力所能及给于司机提示。
19、行调要充分发挥司机驾驶技术优势，禁止使用快速缓解功能给于放风司机缩短停车时间。
20、行调应合理下达时刻表，不同车次等级停站应有数量区别并及时根据时刻表安排停车，酌情但不必须对司机停站进行提醒，根据司机要求可适当提早发车，缩短游戏等待时间。
21，行调要及时标注正晚点信息，终到确认信息，及时下达车次给于司机办理乘降时间。做到信息及时有，发车看路况安排。
22，行调在调整道岔，安排停车等会导致信号或限速变化的操作时，应考虑为司机留出操作列车的反应时间和距离，避免产生由调度人为操作直接或间接导致的信号突变或限速突变。
23、调度不应负责为司机处理刷灯事宜，列车遇到区间红灯，在距离信号50-150米停妥前，调度没有必须处理信号的责任，应要求司机看灯运行。
24、对于掉线玩家调度应及时安排后续列车指引和通告全服道路情况，禁止以任何方式拖延掉线玩家恢复存档位置时间，避免存档消失无效。
25、对于频繁进游戏寻找空降点的玩家，调度不应该配合踢出存档，扶持玩家到处空降，为折腾端口提供便利。
26、鼓励各位行调尽量做到：跑车不调度，调度不跑车。
27、移交调度应确认移交双方玩家数列车数一致，没有玩家掉线存档，没有交路办理中，没有玩家正在进本端口，没有明显的列车位置不同步。
28、值班员角色与行调要求一致，不建议调度轻易使用值班员。值班员由调度任命，值班员错误由调度负责承担，请谨慎选择值班员。
29、行调应该遵守编组决定车次，车次决定待遇的准则，在游戏角度上允许适当提高一档限速和车次待遇，禁止盲目下达严重违背列车编组和线路限速的过分夸张的车次与限速。
30，行调应包容部分玩家特别编组和位置进端口游戏，同时有权利根据其特殊性给于特殊停留或行走安排，原则是不影响正常编组，优先保证正常位置进游戏玩家的游戏环境和跑车图定。
31、行调对于无法察觉的安排失误有需要及时根据情况更正，在力求完美的情况下，不能因为失误而放弃调度的场面，应在各种情况下尽力完成补救措施，保证游戏回到正常。
32、以上指引不做为对部署调度部的强制要求，仅有可能作为事故发生后的定责参考，并作为调度技术水平资格考核标准。其他未尽事项，由ORDP群服进行最终解释。
ORDP群服'''
PSZY_Str = '''ORDP群车辆管理指引
1、 ORDP游戏机车支配权由服务器车辆配属数据（与贴图配属无必然关系）决定，各局官员有权对本局配属车辆安置做最终决定。
2、 游戏中发生车辆整备率下降的，车辆配属局可根据监管官判定的事故责任通告对有责肇事局提出赔车协商，协商无果可以报请联席进行强制赔偿申诉。对无责局协商无果，资产官不受理申诉。
3、 资产官受理，则资产官对因为游戏态度玩忽角色职守，放纵随意瞎搞导致的机车整备率下降索赔将行使强制赔车操作。
4、 赔偿车辆支配权性质是永久配属改变，如有局间借租换车协议均行为无报备不予承认。资产官按报备案进行争执仲裁。
5、 租，借，换车备案应公示不少于一个白天无异议后，才可执行实际车辆调配操作，操作一经完成，不在接受任何反对。
6、 因本身游戏操作技术问题导致的机车整备率下降将记录在案，如肇事方多次事故扔未见技术有明显改善也将行使强制赔车操作。
7、 如遇游戏BUG导致的整备率下降或恶意破坏行为，一经查证可以申请恢复机车整备到事故前。对于恶意破坏行为另案调查，严肃处理。
8、 群服独立调查申诉证据，但涉及申诉局有义务和权利提供本方证据支持。是否采纳由群服判定。
9、 群服申诉时效请在监管官判定事故责任通告后24h内提出，逾期资产管有权拒绝受理，因受损车的情况也可能会发生变化。
10、申应诉由局官员或其委托人参与，只允许一人代表本局参与，期间局长同意可以换人，任何阶段派出申应诉人均视为代表本局局长立场，无新证据不接受推翻前任代表意见。
11、本指引未涉及内容，最终解释权归群服所有
ORDP群服'''
JGZY_Str = '''ORDP群监管处罚指引
为保证游戏环境符合ORDP群游戏气氛，规范游戏服务器对违规玩家的处罚，特指定本监管处罚指引，内容如下:
1.游戏监管操作由指定的游戏监察官执行。
2.监管分成5个等级，分别对应不同监管时间。
3.监管期的玩家会在网页头衔位置标明监管等级，任何路局仍需对监管期本局玩家行为担责。
4.监管期结束后，受监管人员有权主动提出解除监管。
5.清除ID适用于多次违反监管指引，违反群规则。
6.A类监管适用于主观态度上故意破坏游戏玩法气氛，侵犯游戏端口、车辆整备、人车配属、扰乱圈定文件等改变游戏基本数据及平台环境的不当行为。
7.B类监管适用于在游戏内过度瞎搞编组，限速，车次。不听调令，严重干扰游戏其他玩家正常行驶，扰乱游戏场次的行为。
8.C类监管适用于游戏内有主要责任的行车事故，路局局长及助理的非恶意的不当调配机车人员行为。
9.D类监管适用于技术原因多次未见改善反复造成游戏事故，导致车辆整备下降，多次擦边违规经过提醒未见改进的量变积累性惩戒。
10.E类监管适用于一切的责任违规或不当行为。轻微偶发违规不当行为应豁免监管处罚。
11.本监管指引所说游戏玩法方向气氛为:按图跑车，模拟驾驶，完成时刻表。提倡进游戏全列编组站内，用编组表达车次期望，车次映射待遇水平。看信号行驶，听调令控车，追求完整正点停靠车站。
12.本监管条例由群服委派监察官实施，局长，部调，管理人员违反或个人组织集体违反罪加一等处罚，如对裁决异议，可报群服申诉。未尽事宜最终解释权归群服所有。
ORDP群服'''
JFZY_Str = '''积分奖励指引
1，库存总积分20%由各局平分，剩余80%分别奖励客货运量排名
2，各排名积分按比例分配奖励
3，每季度进行一次排名奖励，奖励后路局运量清零重置
4，按如下比例奖励：（比例值换算积分不足整数四舍到个位）
5，奖励活动由积分官组办'''
QPZY_Str = '''配车指引
1， 季度配车每季度举行一次，每次时间连续48小时。
2， 配车由局长或局长委托人参与，每局一位代表做最终决策。
3， 可以配换当季度配车活动未被配换过的任意圈定机车
4， 配换不限单数，按报单顺序进行，限一单一辆。
5， 配车活动期间路局间转积分到账，将收取到账局10%入积分库，不予归还。
6， 每单定配后限时5分钟办理支付及机车移交，过期作废。
7， 配定后导致作废三次，取消本季度配换资格。
8， 机车将以当时整备率数值定价
9， 配换属于强制执行，先报先得，原路局无权阻止车辆配换流出
10, 各局参与请根据本局积分值采配。
11，活动由车务官组办'''
DDOZY_Str = '''人员调局指引
1.常规调局需经双方局长及司机本人同意。如有异议司机可使用强制调局流程
2.司机公开提出调局申请24小时，各方局长无答复，默认为同意申请。
3.强制流程只对离局有效，入局不接受强制流程约束，需入局局长同意。
4.强行流程需在地方无配属状态一周。期间人员不得被调动。如涉及调动三方协商同意，可终止强制，转回常规流程办理
5.局长调局应先辞去局长职务，以局员身份调局。
6.原局局长职位空缺，调局应等新局长产生，由新局长跟进，也可走强制流程，强制流程七天后依然无局长，由人事官代理空缺局局长办理离局操作或入局操作
7.升任局长属于晋升操作，由管委会任命。不受本指引条款管辖。
8.新人入局按玩家意愿直接分派，入局操作不受局长管辖。
9.路局单方执行约束性管理，调离玩家每次都需提供合理理由，且每次不得超过七天。期间未经原局同意，其他局不得调走人员'''
FDZY_Str = '''ORDP服定车次规则
1.服定车次分为部开服定与局开服定两类。
2.部开服定由路局自行上报申请局定升格为部定。局开服定由路局上报图定官审核开行。
3.单局服定车次可选任何线路任何站间，任何里程开行
4.服定车次之间应避免区段重复，车次类型重复，冗余开行。
5. 服定车次每列终到，开行局获得服定运量奖励。多局开行按总量平均奖。
6.服定车次每列未到达，开行局路局扣除相应运量，多局开行按总量平均扣。
7.服定车次每列可由任何玩家担当牵引运行。 服定每列车运量奖罚按季度结算。
8.服定车次每公里与运量奖励按比例计算，相关系数：货车1:20，快速普客1:16，特快行邮1:13，重载货车1:10，动车城际1:8，高铁1:5.
9.车次总里程以游戏线路距离为准，总里程每超过500公里系数加1，部开服定车次本身系数加1。
10.多局开行服定系数增加，增加值为联合局数减一 服定车次每局上限开行五趟，联合开行需占用其中一局指标。
11.季度中可变更从未始发过车次。
12.任何司机累计三次始发服定车次，未实施有效牵引视为故意瞎搞。监管后计数清零。
13.多局联合开行服定，最低牵引里程为150公里乘以路局数。
14.有效牵引里程为服定车次全程里程四分之一。
管委会负责最终解释玩法。
2021.3.16'''
LKJZY_Str = '''ORDP群服务器LKJ信息设置教程
IC卡号：
1.使用字母ID连接ORDP群服务器123.206.56.54进入游戏。
2.初次使用ORDP如申请时无指定，游戏将默认密码123456。
3.鼠标点击设定按钮，打开蓝色输入框。
4.鼠标点击左右按钮，翻页到 IC卡号页面。
5.通过数字键输入密码（你的密码）。
6.鼠标点击转储按钮，完成密码输入。
7.如需修改密码，只需在获得司机号后再次输入新的IC卡号。
8. 鼠标点击转储按钮，完成密码修改。

列车信息：
1.鼠标点击设定按钮，开启蓝色信息输入框
2.通过点击左右按键进行输入信息的翻页
3.在车次输入页面通过点击上下按键输入不同的车次信息
4.在输入信息前可点击查询按键打开蓝色信息列表窗口，按照窗口内信息输入即可。
5.在输入信息时如果填写错误可点击查询按钮清除并重新填写
6.车站号目前可以随意输入。
7.换长输入时忽略小数点，输入全部数字。
8.特殊车次前缀F,O请用LKJ左侧红色解锁和缓解按键输入，分隔斜杠请用设定键输入
9.全部信息输入好后点击确定提交信息。翻到退出点确定关闭蓝色输入窗口。
10.信息输入完整按压开车键后将不会再有语音提示需要输入参数。

抄收调度命令：
1.看到调度命令点击设定按键打开抄收窗口
2.通过数字按键输入相应调度命令号
3.填写错误按查询清除重新输入
4.最后点击确认提交，程序自动关闭输入窗口。

提示：
1.ORDP 版本并用ORDP群服才有司机中文信息和LKJ相关输入功能。
2.有中文名被识别，如果没有获得司机号将无法开车和调度。
3.IC卡号其实就是你的ID保护密码。
ORDP群服务器
ORDP
2020.4.17'''
BZZY_Str = '''ORDP编组指引
为明确游戏编组使用，减少瞎搞编组争议，特拟订如下游戏编组指引:
1. 游戏编组合理性由列车编组本身，编组获得的车次限速，及编组在游戏的待遇三部分组成。
2. 列车编组本身可以使用全部圈定并通过游戏加载校验的车辆组成编组。
3. 没有煤水车的蒸汽，机车属性的车厢，列车两端没有机车的编组，不成组使用的动车组，不能作为可操纵车在游戏内使用。
4. 编组合理的限速由车底最低限速车厢决定，同时结合游戏线路的合理限速。
5. 车次应区分动车组，客车，货车，路用车分类，具体车次应与行车组织待遇相符合，同样编组可有不同运用车次模式。
6. 货物编组长度以游戏始发站不超出股道前后信号机为准，机车使用以全列不大于五台为准，客车编组长度以不超过24辆为准，动车组客运需成组使用且重联不超过两组。以上均含机车。
7. 提倡编组决定车次，车次决定待遇，玩家带任何编组进游戏，待遇给予对应待遇，默认玩家使用编组即接受并理解其待遇。
8. 任何游戏场次，均以普适性运行客货列车为最优先列车，其他不同程度特殊编组待遇应遵从普适性优先列车要求，优先级与特殊度成反比。
9. 不应以编组不合理踢人，单纯编组不存在合理与否的意义，需结合车次待遇判断。有理由的长期停车等待被视为合理安排。
10. 综上所述编组是否瞎搞，由使用编组司机与游戏调度一同负责，违规与否由调度司机共同构成。
ORDP管委会 2021.3'''
CD_Str = '''查询机车+机车号、机车种类、所属局
查询图定信息+车次
查询图定详情+x年x月x日开行+车次
查询司机+中文名或者英文名
查询放风司机+中文名或者英文名
查询放风机车+机车号
查询图定奖励+局
查询运量(+局)
查询端口
查询局长
查询监管
查询部调
今日信息
指引类型+指引
注：加号不用输
如有任何问题 请发送邮件到 2691325401@qq.com'''


def isAllChinese(s):
    for c in s:
        if not ('\u4e00' <= c <= '\u9fa5'):
            return False
    return True


def subtime(date1, date2):
    date1 = datetime.datetime.strptime(date1, "%Y/%m/%d %H:%M:%S")
    date2 = datetime.datetime.strptime(date2, "%Y/%m/%d %H:%M:%S")

    return date2 - date1


def sql_sjxx(input):
    try:
        db = pymysql.connect(
            host="123.206.56.54",
            user="chaxun",
            password="cha13579",
            port=3306,
            database="yxb2",
            charset="utf8"
        )
        cursor = db.cursor()
        if input.isdecimal():
            sql = f"SELECT * FROM sijixinxi WHERE sijihao='{input}';"
        elif isAllChinese(input):
            sql = f"SELECT * FROM sijixinxi WHERE idna='{input}';"
        else:
            sql = f"SELECT * FROM sijixinxi WHERE iden='{input.upper()}';"
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        if len(results) > 0:
            sj = results[0]
            strr = f'''ID：{sj[0]}
司机号：{sj[9]}
名字：{sj[3]}
配属：{sj[1]}
头衔：{sj[2]}
司机分：{round(sj[4], 3)}
调度分：{sj[5]}
等级：{sj[8]}
客运量：{sj[11]}
货运量：{sj[12]}
最后上线时间：{sj[6]}
注册日期：{sj[10]}'''
            return strr
        else:
            db.close()
            return "未查询到该司机"
    except Exception as e:
        print("查询司机报错：" + str(e))
        return "查询司机出错：" + str(e)
    # 关闭数据库连接


def sql_jcxx(input):
    try:
        db = pymysql.connect(
            host="123.206.56.54",
            user="chaxun",
            password="cha13579",
            port=3306,
            database="yxb2",
            charset="utf8"
        )
        cursor = db.cursor()
        if isAllChinese(input):
            sql = f"SELECT * FROM chekuang WHERE CARDW ='{input}';"
        else:
            sql = f"SELECT * FROM chekuang WHERE CARNAME LIKE'%{input}%';"
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        if len(results) > 0:
            i = 0
            strr = ""
            while i < len(results):
                strrr = f"机车：{results[i][0]} 配属：{results[i][1]} 整备率：{results[i][2]}\r\n"
                strr = strr + strrr
                i = i + 1
            db.close()
            return strr
        else:
            db.close()
            return "未查询到该机车"
    except Exception as e:
        print("查询机车报错：" + str(e))
        return "查询机车出错：" + str(e)


def sql_sjff(input):
    # try:
        db = pymysql.connect(
            host="123.206.56.54",
            user="chaxun",
            password="cha13579",
            port=3306,
            database="yxb2",
            charset="utf8"
        )
        cursor = db.cursor()
        if input.isdecimal():
            sql = f"SELECT * FROM sijixinxi WHERE sijihao='{input}';"
        elif isAllChinese(input):
            sql = f"SELECT * FROM sijixinxi WHERE idna='{input}';"
        else:
            sql = f"SELECT * FROM sijixinxi WHERE iden='{input.upper()}';"
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        if len(results) > 0:
            sql = f"SELECT * FROM carlog WHERE ID LIKE '%{results[0][0]}%'"
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            if len(results) > 0:
                strr = ""
                resultsl = list(results)
                resultsl.reverse()
                for i in resultsl[:5]:
                    strr = strr + i[0] + "\r\n"
                db.close()
                strr += f"放风记录共{len(results)}条"
                return strr
            else:
                db.close()
                return input + "没有放风记录"
        else:
            db.close()
            return "未查询到该司机"
    # except Exception as e:
    #     print("查询司机放风报错：" + str(e))
    #     return "查询司机放风出错：" + str(e)


def sql_dkxx():
    try:
        db = pymysql.connect(
            host="123.206.56.54",
            user="chaxun",
            password="cha13579",
            port=3306,
            database="yxb2",
            charset="utf8"
        )
        cursor = db.cursor()
        sql = f"SELECT * FROM serinfo;"
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        strr = ""
        i = 0
        while i < len(results):
            if int(results[i][5]) > 0:
                if results[i][1] == "onn":
                    strrr = f"端口号：{results[i][0]} 欢迎加入\r\n线路：{results[i][2]}\r\n调度：{results[i][4]}\r\n玩家数：{results[i][5]} " \
                            f"\r\n开始时间：{results[i][7]}\r\n"
                else:
                    strrr = f"端口号：{results[i][0]} {results[i][1]}\r\n线路：{results[i][2]}\r\n调度：{results[i][4]}\r\n玩家数：{results[i][5]} " \
                            f"\r\n开始时间：{results[i][7]}\r\n"
            else:
                strrr = f"端口号：{results[i][0]} 空闲中\r\n"
            strr += strrr
            if i != (len(results) - 1):
                strr += "----------------------------------\r\n"
            i = i + 1
        db.close()
        return strr
    except Exception as e:
        print("查询端口报错：" + str(e))
        return "查询端口出错：" + str(e)


def sql_jcff(input):
    try:
        db = pymysql.connect(
            host="123.206.56.54",
            user="chaxun",
            password="cha13579",
            port=3306,
            database="yxb2",
            charset="utf8"
        )
        cursor = db.cursor()
        sql = f"SELECT * FROM carlog WHERE ID LIKE '%{input}%'"
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        if len(results) > 0:
            strr = ""
            resultsl = list(results)
            resultsl.reverse()
            for i in resultsl[:5]:
                strr = strr + i[0] + "\r\n"
            db.close()
            strr+=f"放风记录共{len(results)}条"
            return strr
        else:
            db.close()
            return "未查询到该机车的放风记录"
    except Exception as e:
        print("放风机车查询报错：" + str(e))
        return "查询放风机车出错：" + str(e)


def sql_tdxc(input):
    try:
        db = pymysql.connect(
            host="123.206.56.54",
            user="chaxun",
            password="cha13579",
            port=3306,
            database="yxb2",
            charset="utf8"
        )
        tdxc_data = input.split("开行")[0].split("年")[0] + "/" + input.split("开行")[0].split("年")[1].split("月")[0].zfill(
            2) + "/" \
                    + input.split("开行")[0].split("年")[1].split("月")[1].split("日")[0].zfill(2)
        tdxc_cc = input.split("开行")[1]
        cursor = db.cursor()
        sql = f"SELECT * FROM yanxu WHERE HYDATA = '{tdxc_data}' AND HYCHECI = '{tdxc_cc}';"
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        if len(results) > 0:
            tdxc_sf = results[0][2]
            tdxc_zd = results[0][3]
            tdxc_zt = results[0][5]
            sql = f"SELECT * FROM chengjianglog WHERE ID LIKE '%>%{tdxc_data}%开行{tdxc_cc}%';"
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results1 = cursor.fetchall()
            if tdxc_zt == "终到":
                sfsj = results1[0][0].split(">")[0] + ":00"
                strr = f"车次：{tdxc_cc}\r\n开行日期：{tdxc_data}\r\n始发：{tdxc_sf}\r\n终到：{tdxc_zd}\r\n" + \
                       results1[0][0].split(">")[0] + " "
                strr = strr + results1[0][0].split(">")[1].split(",")[0] + " " \
                                                                           "" + \
                       results1[0][0].split(">")[1].split(",")[1].split("值乘")[0] + " → "
                i = 1
                while i < len(results1):
                    if "值乘开始" in results1[i][0]:
                        strr = strr + results1[i][0].split("自")[1].split("值乘开始")[0] + "\r\n" + \
                               results1[i][0].split(">")[0] + \
                               " " + results1[i][0].split(">")[1].split("值乘")[0] + " " + \
                               results1[i][0].split("自")[1].split("值乘开始")[0] + " → "
                    i = i + 1
                else:
                    strr = strr + results[0][4] + "站\r\n"
                    zdsj = results1[len(results1) - 1][0].split(">")[0] + ":00"
                    sjc = subtime(sfsj, zdsj)
                if len(str(sjc)) > 9:
                    strr = strr + "历时" + str(sjc).split(":")[0] + "天" + str(sjc).split(", ")[1].split(":")[0] + \
                           "小时" + str(sjc).split(", ")[1].split(":")[1] + "分钟 完整终到"
                else:
                    strr = strr + "历时" + str(sjc).split(":")[0] + "小时" + str(sjc).split(":")[1] + "分钟 完整终到"
                return strr
            elif tdxc_zt == "经停":
                sfsj = results1[0][0].split(">")[0] + ":00"
                strr = f"车次：{tdxc_cc}\r\n开行日期：{tdxc_data}\r\n始发：{tdxc_sf}\r\n终到：{tdxc_zd}\r\n" + \
                       results1[0][0].split(">")[0] + " "
                strr = strr + results1[0][0].split(">")[1].split(",")[0] + " " \
                                                                           "" + \
                       results1[0][0].split(">")[1].split(",")[1].split("值乘")[0] + " → "
                i = 1
                while i < len(results1):
                    if "值乘开始" in results1[i][0]:
                        strr = strr + results1[i][0].split("自")[1].split("值乘开始")[0] + "\r\n" + \
                               results1[i][0].split(">")[0] + \
                               " " + results1[i][0].split(">")[1].split("值乘")[0] + " " + \
                               results1[i][0].split("自")[1].split("值乘开始")[0] + " → "
                    i = i + 1
                else:
                    strr = strr + results[0][4] + "站\r\n"
                    now = datetime.datetime.now()
                    zdsj = now.strftime('%Y/%m/%d %H:%M:%S')
                    sjc = subtime(sfsj, zdsj)
                if len(str(sjc)) > 9:
                    strr = strr + "晚点了" + str(sjc).split(" ")[0] + "天" + str(sjc).split(", ")[1].split(":")[0] + \
                           "小时" + str(sjc).split(", ")[1].split(":")[1] + "分钟 旅客滞留在" + results[0][4] + "站"
                else:
                    strr = strr + "晚点了" + str(sjc).split(":")[0] + "小时" + str(sjc).split(":")[1] + "分钟 旅客滞留在" \
                           + results[0][4] + "站"
                return strr
            elif tdxc_zt == "运行":
                sfsj = results1[0][0].split(">")[0] + ":00"
                strr = f"车次：{tdxc_cc}\r\n开行日期：{tdxc_data}\r\n始发：{tdxc_sf}\r\n终到：{tdxc_zd}\r\n" + \
                       results1[0][0].split(">")[0] + " "
                strr = strr + results1[0][0].split(">")[1].split(",")[0] + " " \
                                                                           "" + \
                       results1[0][0].split(">")[1].split(",")[1].split("值乘")[0] + " → "
                i = 1
                while i < len(results1):
                    if "值乘开始" in results1[i][0]:
                        strr = strr + results1[i][0].split("自")[1].split("值乘开始")[0] + "\r\n" + \
                               results1[i][0].split(">")[0] + \
                               " " + results1[i][0].split(">")[1].split("值乘")[0] + " " + \
                               results1[i][0].split("自")[1].split("值乘开始")[0] + " → "
                    i = i + 1
                else:
                    strr = strr + results[0][4] + "站\r\n"
                    now = datetime.datetime.now()
                    zdsj = now.strftime('%Y/%m/%d %H:%M:%S')
                    sjc = subtime(sfsj, zdsj)
                if len(str(sjc)) > 9:
                    strr = strr + "运行了" + str(sjc).split(" ")[0] + "天" + str(sjc).split(", ")[1].split(":")[0] + \
                           "小时" + str(sjc).split(", ")[1].split(":")[1] + "分钟 列车已经从" + results[0][4] + "站开出"
                else:
                    strr = strr + "运行了" + str(sjc).split(":")[0] + "小时" + str(sjc).split(":")[1] + "分钟 列车已经从" \
                           + results[0][4] + "站开出"
                return strr
        else:
            db.close()
            return "无该车次"
    except Exception as e:
        print("车次详细查询报错：" + str(e))
        return "出错了, 请检查格式：查询图定详情xxxx年xx月xx日开行xxx"


def sql_tdxx(input):
    try:
        db = pymysql.connect(
            host="123.206.56.54",
            user="chaxun",
            password="cha13579",
            port=3306,
            database="yxb2",
            charset="utf8"
        )
        inputd = input.upper()
        cursor = db.cursor()
        sql = f"SELECT * FROM tuding WHERE HYCHECI ='{inputd}';"
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results1 = cursor.fetchall()
        if len(results1) > 0:
            strr = f"车次：{results1[0][0]}\r\n始发：{results1[0][1]}\r\n终到：{results1[0][2]}\r\n" \
                   f"奖励：{results1[0][3]}\r\n开行局：{results1[0][4]}\r\n"
            sql = f"SELECT * FROM yanxu WHERE HYCHECI ='{results1[0][0]}' AND HYSTATS = '终到';"
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results2 = cursor.fetchall()
            if len(results2) > 0:
                strr = strr + f"终到数：{len(results2)}\r\n" + "开行日期：\r\n"
                inini = 0
                while inini < len(results2):
                    strr = strr + results2[inini][0] + "\r\n"
                    inini = inini + 1
                strr = strr + f"已获得奖励：{int(results1[0][3]) * len(results2)}\r\n"
            sql = f"SELECT * FROM yanxu WHERE HYCHECI ='{results1[0][0]}' AND HYSTATS = '经停';"
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results3 = cursor.fetchall()
            if len(results3) > 0:
                strr = strr + f"经停数：{len(results3)}\r\n经停站："
                i = 0
                while i < len(results3):
                    strr = strr + results3[i][4] + " "
                    i = i + 1
                strr = strr + "\r\n"
            sql = f"SELECT * FROM yanxu WHERE HYCHECI ='{results1[0][0]}' AND HYSTATS = '运行';"
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results4 = cursor.fetchall()
            if len(results4) > 0:
                strr = strr + f"运行数：{len(results4)}\r\n运行至："
                i = 0
                while i < len(results4):
                    strr = strr + results4[i][4] + " "
                    i = i + 1
                strr = strr + "\r\n"
            return strr + "已获得奖励仅供参考"
        else:
            return "未查询到该车次"
    except Exception as e:
        print("车次查询报错：" + str(e))
        return "查询图定信息出错：" + str(e)


def sql_tdjl(input):
    if input == "":
        return "该局没有图定车"
    db = pymysql.connect(
        host="123.206.56.54",
        user="chaxun",
        password="cha13579",
        port=3306,
        database="yxb2",
        charset="utf8"
    )
    cursor = db.cursor()
    sql = f"SELECT * FROM tuding WHERE HYKAIJU = '{input}';"
    cursor.execute(sql)
    red_table = cursor.fetchall()
    inti = 0
    output_cc = ""
    output_zjl = 0
    output_zzl = 0
    output_zzd = 0
    while len(red_table) > inti:
        sql = f"SELECT * FROM yanxu WHERE HYCHECI = '{red_table[inti][0]}' AND HYSTATS = '终到';"
        cursor.execute(sql)
        green_table = cursor.fetchall()
        output_zjl += len(green_table) * int(red_table[inti][3])
        output_zzd += len(green_table)
        output_cc = output_cc + str(red_table[inti][0]) + "次 终到" + str(len(green_table)) + "列"
        sql = f"SELECT * FROM yanxu WHERE HYCHECI = '{red_table[inti][0]}' AND HYSTATS != '终到';"
        cursor.execute(sql)
        blue_table = cursor.fetchall()
        if len(blue_table) > 0:
            output_zjl -= len(blue_table) * int(red_table[inti][3])
            output_zzl += len(blue_table)
            output_cc = output_cc + " 滞留" + str(len(blue_table)) + "列\r\n"
        else:
            output_cc = output_cc + "\r\n"
        inti += 1
    sql = f"SELECT * FROM tuding WHERE HYKAIJU LIKE '%{input}%';"
    cursor.execute(sql)
    red_table_d = cursor.fetchall()
    output = "路局:" + input + "局\r\n图定列车" + str(len(red_table_d)) + "列\r\n"
    inti_d = 0
    while len(red_table_d) > inti_d:
        if len(red_table_d[inti_d][4]) > 1:
            sql = f"SELECT * FROM yanxu WHERE HYCHECI = '{red_table_d[inti_d][0]}' AND HYSTATS = '终到';"
            cursor.execute(sql)
            green_table_d = cursor.fetchall()
            if "部" in red_table_d[inti_d][4]:
                output_zjl += len(green_table_d) * int(red_table_d[inti_d][3]) / (len(red_table_d[inti_d][4]) - 1)
            else:
                output_zjl += len(green_table_d) * int(red_table_d[inti_d][3]) / len(red_table_d[inti_d][4])
            output_zzd += len(green_table_d)
            output_cc = output_cc + str(red_table_d[inti_d][0]) + "次 终到" + str(len(green_table_d)) + "列"
            sql = f"SELECT * FROM yanxu WHERE HYCHECI = '{red_table_d[inti_d][0]}' AND HYSTATS != '终到';"
            cursor.execute(sql)
            blue_table_d = cursor.fetchall()
            if len(blue_table_d) > 0:
                if "部" in red_table_d[inti_d][4]:
                    output_zjl -= len(blue_table_d) * int(red_table_d[inti_d][3]) / (len(red_table_d[inti_d][4]) - 1)
                else:
                    output_zjl -= len(blue_table_d) * int(red_table_d[inti_d][3]) / len(red_table_d[inti_d][4])
                output_zzl += len(blue_table_d)
                output_cc = output_cc + " 滞留" + str(len(blue_table_d)) + "列\r\n"
            else:
                output_cc = output_cc + "\r\n"
        inti_d += 1
    output = output + output_cc + f"共终到列车{str(output_zzd)}列\r\n共滞留列车{str(output_zzl)}列\r\n" \
                                  f"共获得奖励{str(output_zjl)}"
    if (len(red_table) + len(red_table_d)) > 0:
        return output
    else:
        return "该局没有图定车"


def sql_jzcx():
    db = pymysql.connect(
        host="123.206.56.54",
        user="chaxun",
        password="cha13579",
        port=3306,
        database="yxb2",
        charset="utf8"
    )
    cursor = db.cursor()
    sql = f"SELECT * FROM sijixinxi WHERE idtx LIKE '%局长%';"
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    strr = ""
    i = 0
    while i < len(results):
        strr = strr + results[i][1] + "局局长：" + results[i][0] + " " + results[i][3] + "\r\n"
        i += 1
    return strr


def sql_jycx():
    db = pymysql.connect(
        host="123.206.56.54",
        user="chaxun",
        password="cha13579",
        port=3306,
        database="yxb2",
        charset="utf8"
    )
    cursor = db.cursor()
    sql = f"SELECT * FROM sijixinxi WHERE idtx LIKE '%级监管%';"
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    strr = ""
    i = 0
    for rst in results:
        strr = strr + rst[1] + "|" + rst[3] + " " + rst[2] + "\r\n"
    if strr:
        return strr
    else:
        return "暂无监管人员"


def sql_bdcx():
    db = pymysql.connect(
        host="123.206.56.54",
        user="chaxun",
        password="cha13579",
        port=3306,
        database="yxb2",
        charset="utf8"
    )
    cursor = db.cursor()
    sql = f"SELECT * FROM sijixinxi WHERE idtx LIKE '部调%';"
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    strr = ""
    i = 0
    while i < len(results):
        strr = strr + results[i][1] + "|" + results[i][3] + " 调度分：" + str(results[i][5]) + "\r\n"
        i += 1
    return strr


def sql_gdcx():
    lb = {}
    db = pymysql.connect(
        host="123.206.56.54",
        user="chaxun",
        password="cha13579",
        port=3306,
        database="yxb2",
        charset="utf8"
    )
    cursor = db.cursor()
    sql = f'SELECT * FROM chengjianglog WHERE ID LIKE "%到达%" and ID LIKE ' \
          f'"{str(time.strftime("%Y/%m/%d", time.localtime()))}%";'
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    if len(results) > 0:
        i = 0
        sj = ""
        while i < len(results):
            jz = results[i][0].split(">")[1]
            if "司机" in jz:
                sj = jz.split("司机")[1].split("值乘")[0]
            elif "玩家" in jz:
                sj = jz.split("玩家")[1].split("担当")[0]
            if sj in lb:
                lb[sj] = lb[sj] + 1
            else:
                lb[sj] = 1
            i = i + 1
        sql = f'SELECT * FROM sijixinxi WHERE iden = "{str(max(lb, key=lb.get))}";'
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results1 = cursor.fetchall()
        strr = f"今天停站最多的司机是{results1[0][1]}|{results1[0][3]}，共到达{lb[max(lb, key=lb.get)]}站\r\n"
    else:
        strr = f"今天还没有司机到达车站\r\n"
    ############################################################################################################
    sql = f'SELECT * FROM carlog WHERE ID LIKE "{str(time.strftime("%Y/%m/%d", time.localtime()))}%";'
    # sql = f'SELECT * FROM carlog WHERE ID LIKE "2021/04/09%";'
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results2 = cursor.fetchall()
    lb = {}
    if len(results2) > 0:
        i = 0
        while i < len(results2):
            jz = results2[i][0].split(">")[1]
            sj = jz.split("驾驶")[0]
            if sj in lb:
                lb[sj] = lb[sj] + 1
            else:
                lb[sj] = 1
            i = i + 1
        sql = f'SELECT * FROM sijixinxi WHERE iden = "{str(max(lb, key=lb.get))}";'
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results3 = cursor.fetchall()
        strr = strr + f"今天放风最多的司机是{results3[0][1]}|{results3[0][3]}，共放风{lb[max(lb, key=lb.get)]}次\r\n"
    else:
        strr = strr + f"今天还没有司机放风\r\n"
    return strr


def sql_yxx(msg):
    msg_in = msg.replace('查询', '')
    if msg_in == '当'or msg_in == '本':
        msg = str(time.strftime("%Y/%m/", time.localtime()))
    else:
        if int(msg_in) > 12 or int(msg_in) < 1:
            return f"哪有{msg_in}月啊"
        elif int(msg_in) > int(time.strftime("%m", time.localtime())):
            return f"还没到{msg_in}月呢"
        else:
            if int(msg_in) < 10:
                msg = str(time.strftime("%Y/", time.localtime())) + '0' + msg_in + "/"
            elif int(msg_in) > 10:
                msg = str(time.strftime("%Y/", time.localtime())) + msg_in + "/"

    lj_table = ['上', '乌', '京', '兰', '南', '呼', '哈', '太', '宁', '广', '成', '昆', '武', '沈', '济', '西', '郑', '青']
    lj_dict = dict()

    for lj in lj_table:
        lj_dict[lj] = {'运行天数': 0, '放风次数': 0}

    db = pymysql.connect(
        host="123.206.56.54",
        user="chaxun",
        password="cha13579",
        port=3306,
        database="yxb2",
        charset="utf8"
    )
    cursor = db.cursor()
    sql = f"SELECT * FROM chengjianglog WHERE ID LIKE '%{msg}%';"
    cursor.execute(sql)
    results = cursor.fetchall()

    run_time = dict()
    for lj in lj_table:
        run_time[lj] = list()
    for jl in results:
        jl_time = jl[0].split(' ')[0]
        jl_msg = jl[0].split('>')[1]
        if jl_msg.startswith("玩家"):
            jl_msg = jl_msg.replace("玩家", '')
            jl_name = jl_msg.split('担当')[0]
        else:
            jl_msg = jl_msg.replace("司机", '')
            jl_name = jl_msg.split('值乘')[0]
        sql = f"SELECT * FROM sijixinxi WHERE iden='{jl_name}';"
        cursor.execute(sql)
        results = cursor.fetchall()
        if len(results) > 0:
            lj_name = results[0][1]
            if lj_name != '地':
                if jl_time not in run_time[lj_name]:
                    run_time[lj_name].append(jl_time)
    for lj in lj_table:
        lj_dict[lj]['运行天数'] = len(run_time[lj])

    sql = f"SELECT * FROM carlog WHERE ID LIKE '%{msg}%';"
    cursor.execute(sql)
    results = cursor.fetchall()
    for jl in results:
        jl = jl[0]
        jl_name = jl.split('>')[1].split('驾驶')[0]
        sql = f"SELECT * FROM sijixinxi WHERE iden='{jl_name}';"
        cursor.execute(sql)
        results = cursor.fetchall()
        if len(results) > 0:
            lj_name = results[0][1]
            if lj_name != '地':
                lj_dict[lj_name]['放风次数'] += 1

    send_msg = ""
    for lj in lj_table:
        send_msg += f"{lj}局 {msg_in}月共运行{lj_dict[lj]['运行天数']}天"
        if lj_dict[lj]['放风次数'] == 0:
            send_msg += f" 安全运行\r\n"
        else:
            send_msg += f" 放风{lj_dict[lj]['放风次数']}次\r\n"
    send_msg += "查询系统调试中，如有问题 请联系管理员"
    return send_msg

def sql_ylb(msg):
    db = pymysql.connect(
        host="123.206.56.54",
        user="chaxun",
        password="cha13579",
        port=3306,
        database="yxb2",
        charset="utf8"
    )
    cursor = db.cursor()
    sql = f"SELECT * FROM luju WHERE JUID LIKE '%{msg}%';"
    cursor.execute(sql)
    results = cursor.fetchall()
    send_msg = ""
    for res in results:
        send_msg += f"{res[0]}局:\r\n  客运:{res[1]}\r\n  货运:{res[2]}\r\n  图定:{res[3]}\r\n"
    if send_msg:
        return send_msg
    else:
        return "请输入正确的路局"

