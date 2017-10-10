def main():
        count = 0
        with open("iowa-liquor-sample.csv", "r") as infile:
                for line in infile:
                        line = line.lower()
                        if "single malt scotch" in line:
                                count +=1
        print count
main()
