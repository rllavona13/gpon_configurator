from flask import Flask, render_template, request
import BeautifulSoup

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def gpon_form():

    if 'submit' in request.form:

        gpon_position = '\nonu set ' + (request.form['SlotPosition']) + '/' + (request.form['OLTPosition']) \
                        + '/' + (request.form['ONTPosition']) + ' ' + 'meprof zhone-2426' ' ' \
                        + (request.form['SernoID']) + '\n'

        gpon_traps = 'onu traps enable ' + (request.form['SlotPosition']) + '/' + (request.form['OLTPosition']) \
                     + '/' + (request.form['ONTPosition']) + ' phy,ont,line' + '\n'

        gpon_com_prof = 'cpe system add ' + (request.form['SlotPosition']) + '/' + (request.form['OLTPosition']) \
                        + '/' + (request.form['ONTPosition']) + ' sys-common-profile Default' + '\n'

        gpon_identity = 'cpe system sysinfo add ' + (request.form['SlotPosition']) + '/' \
                        + (request.form['OLTPosition']) \
                        + '/' + (request.form['ONTPosition']) \
                        + ' name "' + (request.form['CustomerName']) + '" location '  \
                        + (request.form['SlotPosition']) + '/' + (request.form['OLTPosition']) \
                        + '/' + (request.form['ONTPosition'])

        gpon_pppoe_bridge = '\nbridge add 1-1-' + (request.form['OLTPosition']) + '-' + (request.form['ONTPosition']) \
                            + '/gpononu gtp 5 downlink-pppoe ' \
                            + 'vlan 351 tagged eth all wlan 1 ' \
                            + 'rg-bpppoe name ' \
                            + (request.form['CustomerName']) + '-PPPoE' + '\n'

        gpon_pppoe = 'cpe rg wan modify ' + (request.form['SlotPosition']) + '/' + (request.form['OLTPosition']) \
                     + '/' + (request.form['ONTPosition']) + ' pppoe-usr-id ' + (request.form['pppoeusername']) \
                     + ' pppoe-password ' + (request.form['pppoepassword']) + ' pppoe-auth pap' + '\n'

        gpon_lan = 'cpe rg lan modify 1/4/2 eth 1 ip-addr 192.168.23.1' + '\n'

        gpon_sip_bridge = '\nbridge add 1-1-' + (request.form['OLTPosition']) + '-' + (request.form['ONTPosition']) \
                            + '/gpononu gtp 1100000001 downlink-voice vlan 10 tagged ' \
                            + 'sip rg-bridged name "' \
                            + (request.form['CustomerName']) + '-VOICE"' + '\n'

        gpon_sip1 = 'cpe voip add ' + (request.form['SlotPosition']) + '/' + (request.form['OLTPosition']) \
                    + '/' + (request.form['ONTPosition']) + '/1' + ' dial-number ' + (request.form['sipuser1']) \
                    + ' username ' + (request.form['sipuser1']) + ' password ' + (request.form['sippassword1']) \
                    + ' voip-server-profile 1' + '\n'

        gpon_sip2 = 'cpe voip add ' + (request.form['SlotPosition']) + '/' + (request.form['OLTPosition']) \
                    + '/' + (request.form['ONTPosition']) + '/2' + ' dial-number ' + (request.form['sipuser2']) \
                    + ' username ' + (request.form['sipuser2']) + ' password ' + (request.form['sippassword2']) \
                    + ' voip-server-profile 1' + '\n'

        return render_template('config.html', gpon_lines=gpon_position + gpon_traps + gpon_com_prof
                               + gpon_identity, gpon_pppoe=gpon_pppoe_bridge + gpon_pppoe + gpon_lan,
                               gpon_voice=gpon_sip_bridge + gpon_sip1 + gpon_sip2)

    else:
        return render_template('index.html')


if __name__ == '__main__':

    app.run(port=5000, debug=True)
