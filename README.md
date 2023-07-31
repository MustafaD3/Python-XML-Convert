# Python-XML-Convert  
Dict To XML  
Function Invoke With Parametr:
```python
to_xml({'product': {'variations': {'variation': {'color': 'Kırmızı', 'body-size': {'body-size-value': ['s'], 'body-size-count': ['0']}}}, 'name': 'Yırtmaçlı Mini Saten Elbise Kırmızı', 'price-not-discounted': '199,99', 'price': '149,99 '}},"products"))
```
Return:
```xml
<products>
    <product>
      <name>Yırtmaçlı Mini Saten Elbise Kırmızı</name>
      <price>149,99 </price>
      <price-not-discounted>199,99</price-not-discounted>
      <variations>
        <variation>
          <body-size>
            <body-size-count>0</body-size-count>
            <body-size-value>s</body-size-value>
          </body-size>
          <color>Kırmızı</color>
        </variation>
      </variations>
    </product>
<products/>
```
