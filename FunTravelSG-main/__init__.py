from Forms import CreateReminderForm, transactionform, PackageForm, key_info
from flask import *
import Reminder, transactions, key_info
import shelve
import Package

app = Flask(__name__)


@app.route('/')
def New_User_Home():
    return render_template('NewUserHome.html')


@app.route('/NewUserPackages')
def New_User_Packages():
    return render_template('NewUserPackages.html')


@app.route('/NewUserAboutUs')
def New_User_About_Us():
    return render_template('NewUserAboutUs.html')


@app.route('/CustomerConfirmation')
def confirmation():
    return render_template('CustomerConfirmation.html')


@app.route('/NewUserEmail')
def New_User_Email():
    return render_template('NewUserEmail.html')


@app.route('/NewUserChatbot')
def New_User_Chatbot():
    return render_template('NewUserChatbot.html')


@app.route('/NewUserMainLogin')
def New_User_Main_Login():
    return render_template('NewUserMainLogin.html')


@app.route('/newusersignup')
def New_User_signup():
    return render_template('newusersignup.html')


@app.route('/customerlogin')
def customer_login():
    return render_template('customerlogin.html')


@app.route('/stafflogin')
def staff_login():
    return render_template('stafflogin.html')


@app.route('/CustomerHome')
def customer_home():
    return render_template('CustomerHome.html')


@app.route('/createTransaction', methods=['GET', 'POST'])
def create_transaction():
    CreateTransactionForm = transactionform(request.form)
    if request.method == 'POST' and CreateTransactionForm.validate():
        transaction_dict = {}
        db = shelve.open('transactions.db', 'c')

        try:
            transactions_dict = db['transactions']
        except:
            print("Error in retrieving transactions from transactions.db.")

        transaction = transactions.transactions(CreateTransactionForm.card_name.data, CreateTransactionForm.card_number.data, CreateTransactionForm.expiry.data, CreateTransactionForm.cvc.data, CreateTransactionForm.default_card.data, CreateTransactionForm.remeber_card.data)
        transactions_dict[transaction.get_transaction_id()] = transaction
        db['Transaction'] = transactions_dict

        db.close()

        return redirect(url_for('retrieve_Transaction'))
    return render_template('CustomerTransactionForm.html', form=CreateTransactionForm)


@app.route('/CustomerCart')
def Customer_Cart():
    key_info_dict = {}
    db = shelve.open('key_info.db', 'r')
    key_info_dict = db['key_info']
    db.close()

    key_info_list = []
    for key in key_info_dict:
        reminder = key_info_dict.get(key)
        key_info_list.append(key_info)

    return render_template('CustomerCart.html', count=len(key_info_list), key_info_list=key_info_list)


@app.route('/CustomerKeyInInformation', methods=['GET', 'POST'])
def key_info():
    Createinfo = key_info(request.form)
    if request.method == 'POST' and Createinfo.validate():
        key_info_dict = {}
        db = shelve.open('key_info.db', 'c')

        try:
            key_info_dict = db['key_info']
        except:
            print("Error in retrieving key_info from key_info.db.")

        info = key_info.key_info(key_info.Infant.data,
                                 key_info.Child.data,
                                 key_info.Adult.data)
        key_info_dict[key_info.get_key_info_id()] = info
        db['package'] = key_info_dict

        db.close()

        return redirect(url_for('Staff_Package_Picker'))
    return render_template('StaffPackageCreator.html', form=Createinfo)


@app.route('/CustomerAboutUs')
def Customer_About_Us():
    return render_template('CustomerAboutUs.html')


@app.route('/CustomerEmail')
def Customer_Email():
    return render_template('CustomerEmail.html')


@app.route('/CustomerChatbot')
def Customer_Chatbot():
    return render_template('CustomerChatbot.html')


@app.route('/CustomerNotifications')
def Customer_Notifications():
    return render_template('CustomerNotifications.html')


@app.route('/CustomerProfile')
def Customer_Profile():
    return render_template('CustomerProfile.html')


@app.route('/StaffHome')
def staff_home():
    return render_template('StaffHome.html')


@app.route('/StaffAboutUs')
def Staff_About_Us():
    return render_template('StaffAboutUs.html')


@app.route('/StaffEmail')
def Staff_Email():
    return render_template('StaffEmail.html')


@app.route('/StaffChatbot')
def Staff_Chatbot():
    return render_template('StaffChatbot.html')


@app.route('/StaffCustomerDatabase')
def Staff_Customer_Database():
    return render_template('StaffCustomerDatabase.html')


@app.route('/StaffStaffDatabase')
def Staff_Staff_Database():
    return render_template('StaffStaffDatabase.html')


@app.route('/StaffAuditLogs')
def Staff_Audit_Logs():
    return render_template('StaffAuditLogs.html')


@app.route('/StaffCreatingNotifications')
def Staff_Creating_Notifications():
    return render_template('StaffCreatingNotifications.html')


@app.route('/StaffRetrievingNotifications')
def Staff_Retrieving_Notifications():
    return render_template('StaffRetrievingNotifications.html')


@app.route('/logout')
def log_out():
    return render_template('logout.html')


@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/createReminder', methods=['GET', 'POST'])
def create_reminder():
    create_reminder_form = CreateReminderForm(request.form)
    if request.method == 'POST' and create_reminder_form.validate():
        reminders_dict = {}
        db = shelve.open('reminder.db', 'c')

        try:
            reminders_dict = db['Reminders']

        except:
            print("Error in retrieving reminders from reminder.db.")

        reminder = Reminder.Reminder(create_reminder_form.name.data, create_reminder_form.reminder_type.data,
                                     create_reminder_form.information.data)
        reminders_dict[reminder.get_reminder_id()] = reminder
        db['Reminders'] = reminders_dict

        # Test Codes
        reminders_dict = db['Reminders']
        reminder = reminders_dict[reminder.get_reminder_id()]
        print(reminder.get_name(), reminder.get_reminder_type(),
              "was stored in reminder.db successfully with reminder_id ==",
              reminder.get_information())

        db.close()

        return redirect(url_for('retrieve_reminders'))
    return render_template('createReminder.html', form=create_reminder_form)


@app.route('/retrieveReminder')
def retrieve_reminders():
    reminders_dict = {}
    db = shelve.open('reminder.db', 'r')
    reminders_dict = db['Reminders']
    db.close()

    reminders_list = []
    for key in reminders_dict:
        reminder = reminders_dict.get(key)
        reminders_list.append(reminder)

    return render_template('retrieveReminder.html', count=len(reminders_list), reminders_list=reminders_list)


@app.route('/updateReminder/<int:id>/', methods=['GET', 'POST'])
def update_reminder(id):
    update_reminder_form = CreateReminderForm(request.form)
    if request.method == 'POST' and update_reminder_form.validate():
        reminders_dict = {}
        db = shelve.open('reminder.db', 'w')
        reminders_dict = db['Reminders']

        reminder = reminders_dict.get(id)
        reminder.set_name(update_reminder_form.name.data)
        reminder.set_reminder_type(update_reminder_form.reminder_type.data)
        reminder.set_information(update_reminder_form.information.data)

        db['Reminders'] = reminders_dict
        db.close()

        return redirect(url_for('retrieve_reminders'))
    else:
        reminders_dict = {}
        db = shelve.open('reminder.db', 'r')
        reminders_dict = db['Reminders']
        db.close()

        reminder = reminders_dict.get(id)
        update_reminder_form.name.data = reminder.get_name()
        update_reminder_form.reminder_type.data = reminder.get_reminder_type()
        update_reminder_form.information.data = reminder.get_information()

        return render_template('updateReminder.html', form=update_reminder_form)


@app.route('/deleteReminder/<int:id>', methods=['POST'])
def delete_reminder(id):
    reminders_dict = {}
    db = shelve.open('reminder.db', 'w')
    reminders_dict = db['Reminders']

    reminders_dict.pop(id)

    db['Reminders'] = reminders_dict
    db.close()

    return redirect(url_for('retrieve_reminders'))


if __name__ == '__main__':
    app.run()
