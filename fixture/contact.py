from model.contact import Contact
import re
from selenium.common.exceptions import NoSuchElementException

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home_phone)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work_phone)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email3)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.phone2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.app.return_to_home_page()
        self.contact_cache = None

    def update_first_contact(self, contact):
        self.update_contact_by_index(0, contact)

    def update_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        # open contact for edit
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        # change contact properties
        wd.find_elements_by_name("firstname")[index].click()
        wd.find_elements_by_name("firstname")[index].clear()
        wd.find_elements_by_name("firstname")[index].send_keys(contact.firstname)
        wd.find_elements_by_name("middlename")[index].clear()
        wd.find_elements_by_name("middlename")[index].send_keys(contact.middlename)
        wd.find_elements_by_name("lastname")[index].clear()
        wd.find_elements_by_name("lastname")[index].send_keys(contact.lastname)
        wd.find_elements_by_name("nickname")[index].clear()
        wd.find_elements_by_name("nickname")[index].send_keys(contact.nickname)
        wd.find_elements_by_name("title")[index].click()
        wd.find_elements_by_name("title")[index].clear()
        wd.find_elements_by_name("title")[index].send_keys(contact.title)
        wd.find_elements_by_name("company")[index].click()
        wd.find_elements_by_name("company")[index].clear()
        wd.find_elements_by_name("company")[index].send_keys(contact.company)
        wd.find_elements_by_name("address")[index].click()
        wd.find_elements_by_name("address")[index].clear()
        wd.find_elements_by_name("address")[index].send_keys(contact.address)
        wd.find_elements_by_name("home")[index].click()
        wd.find_elements_by_name("home")[index].clear()
        wd.find_elements_by_name("home")[index].send_keys(contact.home_phone)
        wd.find_elements_by_name("mobile")[index].click()
        wd.find_elements_by_name("mobile")[index].clear()
        wd.find_elements_by_name("mobile")[index].send_keys(contact.mobile)
        wd.find_elements_by_name("work")[index].click()
        wd.find_elements_by_name("work")[index].clear()
        wd.find_elements_by_name("work")[index].send_keys(contact.work_phone)
        wd.find_elements_by_name("fax")[index].click()
        wd.find_elements_by_name("fax")[index].clear()
        wd.find_elements_by_name("fax")[index].send_keys(contact.fax)
        wd.find_elements_by_name("email")[index].click()
        wd.find_elements_by_name("email")[index].clear()
        wd.find_elements_by_name("email")[index].send_keys(contact.email)
        wd.find_elements_by_name("email2")[index].click()
        wd.find_elements_by_name("email2")[index].clear()
        wd.find_elements_by_name("email2")[index].send_keys(contact.email2)
        wd.find_elements_by_name("email3")[index].click()
        wd.find_elements_by_name("email3")[index].clear()
        wd.find_elements_by_name("email3")[index].send_keys(contact.email3)
        wd.find_elements_by_name("address2")[index].click()
        wd.find_elements_by_name("address2")[index].clear()
        wd.find_elements_by_name("address2")[index].send_keys(contact.address2)
        wd.find_elements_by_name("phone2")[index].click()
        wd.find_elements_by_name("phone2")[index].clear()
        wd.find_elements_by_name("phone2")[index].send_keys(contact.phone2)
        wd.find_elements_by_name("notes")[index].click()
        wd.find_elements_by_name("notes")[index].clear()
        wd.find_elements_by_name("notes")[index].send_keys(contact.notes)
        # save updates
        wd.find_elements_by_xpath("//div[@id='content']/form/input[22]")[index].click()
        self.app.return_to_home_page()
        self.contact_cache = None

    def open_contacts_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//form[@action='/addressbook/']").click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.app.open_home_page()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def select_first_contact(self):
        self.select_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home_phone", contact.home_phone)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work_phone", contact.work_phone)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def modify_first_contact(self, new_contact_data):
        self.modify_contact_by_index(0, new_contact_data)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_first_contact()
        # open modification form
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        # fill contact form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.app.return_to_home_page()
        self.contact_cache = None

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector("tr"):
                try:
                    text = element.find_element_by_name("selected[]").get_attribute("title")
                    id = element.find_element_by_name("selected[]").get_attribute("value")
                    firstname = re.search('\(([^)]+)', text).group(1).split()[0]
                    lastname = re.search('\(([^)]+)', text).group(1).split()[1]
                    self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id))
                except NoSuchElementException:
                    pass
        return list(self.contact_cache)

