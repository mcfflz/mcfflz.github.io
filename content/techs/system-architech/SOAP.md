# 概念

SOAP 协议基于 HTTP 协议，使用 SOAP 格式的 XML 作为 HTTP 报文体。示例如下：

```xml
<?xml version="1.0"?>
<soap:Envelope
xmlns:soap="http://www.w3.org/2001/12/soap-envelope"
soap:encodingStyle="http://www.w3.org/2001/12/soap-encoding">

<soap:Header>
    <!-- 定义应用程序专用信息（比如认证、支付等） -->
    ···
</soap:Header>

<soap:Body>
    <!-- 定义打算传送到消息最终端点的实际 SOAP 消息 -->
    ...
    <soap:Fault>
        <!-- 定义 SOAP 消息的错误和状态信息 -->
        ...
    </soap:Fault>
</soap:Body>

</soap:Envelope>
```

# 完整报文示例

## SOAP REQUEST

```http
POST /InStock HTTP/1.1
Host: www.example.org
Content-Type: application/soap+xml; charset=utf-8
Content-Length: nnn

<?xml version="1.0"?>
<soap:Envelope
xmlns:soap="http://www.w3.org/2001/12/soap-envelope"
soap:encodingStyle="http://www.w3.org/2001/12/soap-encoding">

<soap:Body xmlns:m="http://www.example.org/stock">
  <m:GetStockPrice>
    <m:StockName>IBM</m:StockName>
  </m:GetStockPrice>
</soap:Body>

</soap:Envelope>
```

## SOAP RESPONSE

```http
HTTP/1.1 200 OK
Content-Type: application/soap+xml; charset=utf-8
Content-Length: nnn

<?xml version="1.0"?>
<soap:Envelope
xmlns:soap="http://www.w3.org/2001/12/soap-envelope"
soap:encodingStyle="http://www.w3.org/2001/12/soap-encoding">

<soap:Body xmlns:m="http://www.example.org/stock">
  <m:GetStockPriceResponse>
    <m:Price>34.5</m:Price>
  </m:GetStockPriceResponse>
</soap:Body>

</soap:Envelope>
```

