import anvil.server
from anvil.tables import app_tables
import unittest


@anvil.server.callable
def store_line_data(people, time_taken, party):
    app_tables.line_data.add_row(party=party, people=people, time_taken=time_taken)
    return "Data stored successfully."


@anvil.server.callable
def estimate_line_time(current_people, party):
    all_data = app_tables.line_data.search(party=party)
    total_people = 0
    total_time = 0

    for data in all_data:
        total_people += data["people"]
        total_time += data["time_taken"]

    if total_people == 0:
        return "Insufficient data for this party."

    avg_time_per_person = total_time / total_people
    estimated_time = avg_time_per_person * current_people

    return f"Estimated time: {estimated_time} minutes"

#http://your-anvil-app-url/_/api/query/{party}/{estimate}
#http://gcp.zanzalaz.com:6060/_/api/query/{party}/{estimate}
@anvil.server.http_endpoint('/query/:party/:estimate')
def query_line_data(estimate, party):
    results = estimate_line_time(estimate, party)
    return {'estimate': results}


# Unit Test
class TestLineFunctions(unittest.TestCase):

    def test_store_line_data(self):
        result = store_line_data(10, 20, "fake")
        self.assertEqual(result, "Data stored successfully.")

    def test_estimate_line_time(self):
        store_line_data(10, 20, "fake")
        store_line_data(20, 40, "fake")
        result = estimate_line_time(15, "fake")
        self.assertEqual(result, "Estimated time: 30.0 minutes")


if __name__ == "__main__":
    anvil.server.connect("YOUR_ANVIL_UPLINK_KEY")
    unittest.main()