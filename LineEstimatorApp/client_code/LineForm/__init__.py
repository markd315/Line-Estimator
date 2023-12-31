import anvil
from anvil import *

class LineForm(HtmlPanel):

    def __init__(self, **properties):
        super().__init__()
        self.clear()
        self.html = "@theme:assets:standard-page.html"
        self.content_panel = GridPanel()
        # Initialize components
        # Initialize components
        self.lbl_party = Label(text="Party ID:")
        query_dict = get_url_hash()
        print(query_dict)
        if query_dict == '' or query_dict is None or query_dict["party"] is None:
            initial_party = ''
        else:
            initial_party = query_dict["party"]

        self.txt_party = TextBox(placeholder="Enter PartyID for your line", text=initial_party)

        self.lbl_people = Label(text="People in line when you joined the line:")
        self.txt_people = TextBox(placeholder="Enter People")

        self.lbl_time_taken = Label(text="Time Taken for you to reach front:")
        self.txt_time_taken = TextBox(placeholder="Enter Time Taken")

        self.lbl_current_people = Label(text="Current People in line for estimation:")
        self.txt_current_people = TextBox(placeholder="Enter Current People")

        self.btn_store_data = Button(text="Store Data")
        self.btn_estimate_time = Button(text="Estimate Time")
        self.lbl_estimate = Label()

        # Set up event handlers
        self.btn_store_data.set_event_handler('click', self.btn_store_data_click)
        self.btn_estimate_time.set_event_handler('click', self.btn_estimate_time_click)

        # Add components to form
        self.add_component(self.lbl_party)
        self.add_component(self.txt_party)

        self.add_component(self.lbl_people)
        self.add_component(self.txt_people)

        self.add_component(self.lbl_time_taken)
        self.add_component(self.txt_time_taken)

        self.add_component(self.btn_store_data)

        self.add_component(self.lbl_current_people)
        self.add_component(self.txt_current_people)

        self.add_component(self.btn_estimate_time)
        self.add_component(self.lbl_estimate)

    def btn_store_data_click(self, **event_args):
        party = self.txt_party.text
        people = int(self.txt_people.text)
        time_taken = int(self.txt_time_taken.text)
        anvil.server.call('store_line_data', people, time_taken, party)

    def btn_estimate_time_click(self, **event_args):
        party = self.txt_party.text
        current_people = int(self.txt_current_people.text)
        estimated_time = anvil.server.call('estimate_line_time', current_people, party)
        self.lbl_estimate.text = estimated_time