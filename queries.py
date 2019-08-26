QUERIES = {
        "review_save": "INSERT INTO review (`name`, `emailid`, `message`) VALUES (%(name)s, %(emailid)s, %(message)s)",
        "review_get_all": "SELECT * FROM review"
}
