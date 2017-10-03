class FBPage:
    
    def __init__(self, page_type, page_name):
        self.page_type = page_type
        self.page_name = page_name


def create_page():
    fbpage_category = ["advertising", "agriculture", "airport", "bussiness", "hotel", "hospital", "doctor"]
    print("Categories: {}".format(",".join(fbpage_category)))
        #join takes a list & prints it as a comma-separated string
    fbpage_type = ["Local", "Company", "Brand", "Artist", "Entertainment", "Community"]
    choice = input("Enter an page to create (Local, Company, Brand, Artist, Entertainment, Community): ")
    if choice in fbpage_type:
        page_name = input("Enter Page Name: ")
        page_category = input("Choose a Category: ")

        fbpage = FBPage(page_category, page_name)
        print("Created FB {} Page".format(page_category))


create_page()