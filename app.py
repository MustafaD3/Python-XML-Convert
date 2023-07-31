import json
def to_xml(d,container="products",indent="  "):
   def _to_xml(d, ind, p = None):
      if not isinstance(d, (dict, list)):
         yield f'{ind}<{p}>{d}</{p}>'
      elif isinstance(d, list):
         for i in d:
            yield from _to_xml(i, ind, p)
      else:
          p1, p2 = '' if p is None else f'{ind}<{p}>\n', '' if p is None else f'\n{ind}</{p}>'
          ind = ind if p is None else ind+indent
          for i in sorted(d): #sorting the keys
             if not isinstance(d[i], (dict, list)):
               
                yield f'{p1}{ind}<{i}>{d[i]}</{i}>{p2}'
             elif isinstance(d[i], dict):
            
                yield '{}{}<{}>\n{}\n{}</{}>{}'.format(p1, ind, i, '\n'.join(_to_xml(d[i], ind+indent)), ind, i, p2)
             else:
                
                yield from _to_xml(d[i], ind, p = i)
   return '<{}>\n{}\n<{}/>'.format(container,'\n'.join(_to_xml(d, indent)),container)
#Example Output
jsonData = json.loads(json.dumps({"product": {"variations": {"variation": {"color": "K\u0131rm\u0131z\u0131", "body-size": {"body-size-value": ["s"], "body-size-count": ["0"]}}}, "name": "Y\u0131rtma\u00e7l\u0131 Mini Saten Elbise K\u0131rm\u0131z\u0131", "price-not-discounted": "199,99", "price": "149,99 "}}))
print(to_xml(jsonData,"products"))