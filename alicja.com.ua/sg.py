import csv
from sys import argv

def main():
    
    """
    pc for Alicja v1.0
    Generate test cases for addin new position for alicja.com.ua
    """
    # product classes
    product_clasifier = {}
    with open("types.txt", 'r') as types:
        for t in types:
            key, val = t.split(';')
            product_clasifier[key] = val
    # 
    with open("info.csv", 'rb') as main_f:
        test_cases = []
        
        with open("test case prototype.html", 'r') as test_case_prototype:
            all_records = csv.reader(main_f, delimiter=";")
            
            all_test_case_lines = "".join(test_case_prototype.readlines())
            
            for row in all_records:
                name = unicode(row[0], "cp1251").encode("utf-8")
                article = row[1]
                consistance = unicode(row[2], "cp1251").encode("utf-8")
                price = row[3]
                product_class = unicode(product_clasifier[row[5]], "cp1251").encode("utf-8")
                photos = row[6].split(",")
                test_cases.append("article_" + article)
                
                # open new file
                with open("article_" + article + ".html", 'w') as test_case:
                    
                    # Add photos
                    photo_counter = 0
                    images_str = ""
                    for photo in photos:
                        images_str += \
                        ('<tr>\n'+\
                        '\t<td>type</td>\n'+\
                        '\t<td>name=product_image_{counter}</td>\n'+\
                        '\t<td>D:\\GEorGE\\work\other\\alicja.com.ua\\Alicja\\{photo_name}</td>\n'+\
                        '</tr>\n').format(counter=photo_counter, photo_name = photo)
                        photo_counter += 1
                            
                    # Add static info
                    
                    test_case.write(all_test_case_lines.format(n=name, a=article, p=price, pc=product_class, c=consistance, images=images_str))

        # create test suit
        with open("test_suit.html", 'w') as test_suit:
            with open("test suit prototype.html", 'r') as test_suit_prototype:
                test_cases_text = ""
                for tc in test_cases:
                    test_cases_text += '<tr><td><a href="{filename}.html">{filename}</a></td></tr>\n'.format(filename=tc)
                
                test_suit.write("".join(test_suit_prototype.readlines()).format(test_cases=test_cases_text))
                
            
if __name__ == "__main__":
    main(*argv[1:])