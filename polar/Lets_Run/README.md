# Lets Run Documentation

## Running the program
run the command `docker-compose up` inside Lets_Run dictionary

The program is now serviced using waitress on http://localhost:8080/

## Running Example:

### First Step: Signup users
let's add Romi Ron (31) from Tel Aviv
using _Postman_ I send a post request to the url:
 http://localhost:8080/api/signup
 with the following json as the body of the request
 ```
{
  "name": "Romi Ron",
  "age": 31,
  "city": "Tel Aviv"
}
 ```
 I get in Response a private key (created Randomly using RSA 2048 encryption algorithm) that i can use later to sign requests in the name of Romi Ron:
 ```
 {
    "private_key": "-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEAwjV+x0WB3myvs0hphjd7pVRw7jVpim7Aql1MaHDadoNBSkkL\nnNeWp7rASySoaO6nNCdZSV5Ju/clNiVRM3Zy8Cj5GXfM21TmgX6dmIjjYjQW2qqJ\nlIIBMkUN+78zQgVvSnc6J/mhy/fyOSKbQYZI+R+SEpQ2hd88eIGrKgT7tfn4KvnG\nRjYuZYghuUJSbUuAkqYonTFT1vkjFwUnlqpM/d2jMAyHrsCCIWwQy16kcv6yO9cD\nxJI3Iot4fMYAaV8pVfaD3C9r/4R2CdNNJuBjJK8vhQaGVHcZqkP10bZtZIeZtjNk\nDra1b0FoJev5MUvldla9wDnO8fwUXUA1RbyhWQIDAQABAoIBABAzfJUswBCT5N+3\naY+Cnw7OlFyC2dWXDKffAEnxftVbzhK035egx9bL4PvDyJrMVz17ZNrr1zSA1xAF\nHUOGR5YE96wqDs24mkFw6b5jo625u7MCfqyutbaBr+YcRVnmGyp3922F89CQqW/J\nFRuVE2RY6mDLZXWrMZ+57X35YXLaN3xuyAX2sIiOF+2iYg6k8BAMTYccwCB3igc6\nIWfKpGaU1KoJTcw6abpZPDOpLMDEMUn+vcuwVF/R+hpY165yPkV3Az3GrqU/BCoI\nzi7ZFULUvDyRTpo6lZfQHU4Feyfw48gil0EOgHj0xD1dn2E1gYfVpgY6BMu9eqEW\nz7HhUDMCgYEA3E0zi8C8AErwgpFXnLy3UMZ0IPACCrpy7T8OMyqGb0k2ltefZKwb\n2cxyCMvjBSPc5mPHklNIBTQvCYB4PI/UwWHZVgW6jlgrowOelc/11faQPnjUXwcc\nRLOUOBzbq5SChINa1fzI441QhHSZhwgqa+jLhDmHfrEPW9rhYZOGPqMCgYEA4a3k\nHOCksoNzbUDUKY6RjAkk+lXZ05wLWX8FXuP2h8t2CMz9pXyUyTLZzjSImMueaRrO\n059IHb4Va1NqmZ+fJau9j4JIzKTbkFnUNx4i4nfU1IBd3U8oGPlSh8f4GajvOIDk\nvhEI/hpamHBP3+sjzArmzC4YBiwTH5Ne5EViC9MCgYBjWvoVXF4tr56a9FvUF5SB\nfI9hT31MQ1yTvS11TAeHZziUfTio2apR5w/DAdkoN01oJrYaOy8vEaLpISSZA7FL\nagrv7fN+QSulAHvkSv8veV0Cn9H/7aAFKAx/5hv4XSkkBG3SNoiPf+tBYajgKoGf\nW0V2I9AFBmvL3IJrVHJmCwKBgQC2VsBDEMIhNZISSNnixb0VLuJAnRLFJYQKCFX3\niCpNJ3ezvqSFi7XPJhXSxKFFCudvtmg7las31LgLojcz7kMwtaUQCUz2g5Ce/eU3\nr1KyNe2w0BKG2AjmvLMQ3+G2Icc+mO24H51raTGfjscKfTrMBlbZy7g/bGb7ESAP\nQXvpXwKBgHyrLSMp+hOmJfZjLk7erfQTAGyS4qRhxbNqV4kxxP9DW0Tq+Fs+8U8L\nhjQd1uUcu0uODYbNbX4/8oLyLytwRYjmg9FmQ03h1FuMuCgTqjq9wGa33CPavH0r\njL8/ghizasZgLqICJHPULtTaA4AuUmI1cxPAHrFJ5G8dC3cRb4w2\n-----END RSA PRIVATE KEY-----"
}
```
Lets add two more users:

```
{
  "name": "Dan Dean",
  "age": 28,
  "city": "Tel Aviv"
}
```
```
{
  "name": "Clark Kent",
  "age": 28,
  "city": "Ashdod"
}
```

### Second Step: Update the users total distance
To simulate an application signning a json and encoding the data in base64 I added a new url: http://localhost:8080/api/sign-request
It takes a json of this format
```
{
    "private_key": <private_key>,
    "request": <json object>
}
```
 The reponse is:
 ```
 {
     "request":<"xxxxx.yyyyy">
 }

 xxxxx - is the given json object in base64
 yyyyy - is the signature on the object in base64 using the private key 
 ```

 Now let's create and sign a request to add distance of 10 to Romi Ron.

Call http://localhost:8080/api/sign-request with a json body:

```
{
    "private_key": "-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEAwjV+x0WB3myvs0hphjd7pVRw7jVpim7Aql1MaHDadoNBSkkL\nnNeWp7rASySoaO6nNCdZSV5Ju/clNiVRM3Zy8Cj5GXfM21TmgX6dmIjjYjQW2qqJ\nlIIBMkUN+78zQgVvSnc6J/mhy/fyOSKbQYZI+R+SEpQ2hd88eIGrKgT7tfn4KvnG\nRjYuZYghuUJSbUuAkqYonTFT1vkjFwUnlqpM/d2jMAyHrsCCIWwQy16kcv6yO9cD\nxJI3Iot4fMYAaV8pVfaD3C9r/4R2CdNNJuBjJK8vhQaGVHcZqkP10bZtZIeZtjNk\nDra1b0FoJev5MUvldla9wDnO8fwUXUA1RbyhWQIDAQABAoIBABAzfJUswBCT5N+3\naY+Cnw7OlFyC2dWXDKffAEnxftVbzhK035egx9bL4PvDyJrMVz17ZNrr1zSA1xAF\nHUOGR5YE96wqDs24mkFw6b5jo625u7MCfqyutbaBr+YcRVnmGyp3922F89CQqW/J\nFRuVE2RY6mDLZXWrMZ+57X35YXLaN3xuyAX2sIiOF+2iYg6k8BAMTYccwCB3igc6\nIWfKpGaU1KoJTcw6abpZPDOpLMDEMUn+vcuwVF/R+hpY165yPkV3Az3GrqU/BCoI\nzi7ZFULUvDyRTpo6lZfQHU4Feyfw48gil0EOgHj0xD1dn2E1gYfVpgY6BMu9eqEW\nz7HhUDMCgYEA3E0zi8C8AErwgpFXnLy3UMZ0IPACCrpy7T8OMyqGb0k2ltefZKwb\n2cxyCMvjBSPc5mPHklNIBTQvCYB4PI/UwWHZVgW6jlgrowOelc/11faQPnjUXwcc\nRLOUOBzbq5SChINa1fzI441QhHSZhwgqa+jLhDmHfrEPW9rhYZOGPqMCgYEA4a3k\nHOCksoNzbUDUKY6RjAkk+lXZ05wLWX8FXuP2h8t2CMz9pXyUyTLZzjSImMueaRrO\n059IHb4Va1NqmZ+fJau9j4JIzKTbkFnUNx4i4nfU1IBd3U8oGPlSh8f4GajvOIDk\nvhEI/hpamHBP3+sjzArmzC4YBiwTH5Ne5EViC9MCgYBjWvoVXF4tr56a9FvUF5SB\nfI9hT31MQ1yTvS11TAeHZziUfTio2apR5w/DAdkoN01oJrYaOy8vEaLpISSZA7FL\nagrv7fN+QSulAHvkSv8veV0Cn9H/7aAFKAx/5hv4XSkkBG3SNoiPf+tBYajgKoGf\nW0V2I9AFBmvL3IJrVHJmCwKBgQC2VsBDEMIhNZISSNnixb0VLuJAnRLFJYQKCFX3\niCpNJ3ezvqSFi7XPJhXSxKFFCudvtmg7las31LgLojcz7kMwtaUQCUz2g5Ce/eU3\nr1KyNe2w0BKG2AjmvLMQ3+G2Icc+mO24H51raTGfjscKfTrMBlbZy7g/bGb7ESAP\nQXvpXwKBgHyrLSMp+hOmJfZjLk7erfQTAGyS4qRhxbNqV4kxxP9DW0Tq+Fs+8U8L\nhjQd1uUcu0uODYbNbX4/8oLyLytwRYjmg9FmQ03h1FuMuCgTqjq9wGa33CPavH0r\njL8/ghizasZgLqICJHPULtTaA4AuUmI1cxPAHrFJ5G8dC3cRb4w2\n-----END RSA PRIVATE KEY-----",
    "request": {
        "name": "Romi Ron",
        "distance": 10
    }
}
```

We get in response:
```
{
    "request": "eyJuYW1lIjogIlJvbWkgUm9uIiwgImRpc3RhbmNlIjogMTB9.Kxa3E8Dzw0B62Uy8p4YlO0X+298gl+G7L5WjB7Nx0+UhsY7dVjK66wY1pxZM7FOjfzrFFK638CcXbA7hZr9jQPoq8+Yfex27GEk/KeoE1grONp7NRKhrxJTNaok29uNfasHTInv0sT4d7hVX/TE9kfG20HRsE4V+1c23v7yhY2wbgSi/NpQZ57uwMT5nXFpnoIsSBBBVMyrcatOupGW079vkOoustGIbyKqY3QeOL+X+T6nNuVBSwhSLhPcKciw5b7H4tjUndg88bSqqvcFvc3H4cHqVZ6QcqejfSPekEDdBovZlY2qm1THXNOyezvu8cjaXlitWU6+Lbc2VkTKm7Q=="
}
```

Now we update the total distance of Romi Ron calling the post request http://localhost:8080/api/update with the json:
```
{
    "request": "eyJuYW1lIjogIlJvbWkgUm9uIiwgImRpc3RhbmNlIjogMTB9.Kxa3E8Dzw0B62Uy8p4YlO0X+298gl+G7L5WjB7Nx0+UhsY7dVjK66wY1pxZM7FOjfzrFFK638CcXbA7hZr9jQPoq8+Yfex27GEk/KeoE1grONp7NRKhrxJTNaok29uNfasHTInv0sT4d7hVX/TE9kfG20HRsE4V+1c23v7yhY2wbgSi/NpQZ57uwMT5nXFpnoIsSBBBVMyrcatOupGW079vkOoustGIbyKqY3QeOL+X+T6nNuVBSwhSLhPcKciw5b7H4tjUndg88bSqqvcFvc3H4cHqVZ6QcqejfSPekEDdBovZlY2qm1THXNOyezvu8cjaXlitWU6+Lbc2VkTKm7Q=="
}
```
In Response we get
```
{
    "totalDistanceRun": 10
}
```

we do the same thing to add distance of 20 to Dan Dean and 30 to Clark Kent.

if we try to update an unknown person or we messup the request json the reponse is

```
{
    "totalDistanceRun": -1
}
```

### Step Three: Get the stats
To get the stats about a certain user we need to use the _sign-request_ again to sign a request for stats for the user.
For example lets say i want to know Clark Kent Rank *overall*
Call http://localhost:8080/api/sign-request with a json body (don't forget to use _Clark Kent_ private key):

```
{
    "private_key": "-----BEGIN RSA PRIVATE KEY-----\nMIIEogIBAAKCAQEAlFLupwuX1SuIZ1VIbuxB1iIGo1FLxD+QkM4GxFK1YuaETW0x\nn1QpQ6n+JdpNwdTjrlRKRvwErYnd0qmyySBusuDlneD/leNdjbcDdjRCqOBGZ4Dw\nNB/PBaVvKtqc9kuEr+nWTQFNf/B0HPZvvxZPRxqbmaN4qhz15rlIWyxzkZFrf8s+\n47QyMfYmVYtae00AVmjzJhVjW98a220AtoLFhqv6XSTQr+W45Qakw0iHTl1FfiQj\nS9qbFzNRB82g45oEYT0xWxg6wWBcF+IikRC3bEucsuXKpTdl6fF/MF8r7Qj+GZij\nzGbjAUZDXhZFt1uIPty9Tf35z244c2SbQejegQIDAQABAoIBAADnB0YzaxtULjqI\nuY3ZOKZToywztq0NQPUsl7xyj2F4axYog6yHP9AGVQJIc4AqKi95mlEXv/SJWfTp\n7OlN3faPKT5+a7evADb4RdhehYhPAwamsW9zwRf083n0hg92kqpaVyA1UZIldaNm\neXQVb+qMFiXHaZjJX9KlTnQlj1dzo24f+rJkhbWAXRm3OMmIBNbmXopwkmU6+xIN\nEOteYr3Hf89LEKsSYqK8z58tYEqDCK7Z85osfvkr8uJAP8fTDQI2U/HPlA6omGRx\na+D6ciUcgVQ6iMS6hES8ZWMOZxvUBTm4uygKpQwvHlFiTLKz98bL3yUp1SoWCssk\ncTPeiQECgYEAthxHAoLdBPinTXY4is690A6xTJnnINQgpGeYuoH93UaAK2zEgBFf\nd0VMp1HnzjrMZGmBla74v/jw+YyRGofEVjDsKhCbcsDNS0EkrHBaLmQ07JZ+MB41\noiLq3nd6evMzdrScRNYLOS8NRwPuAIVkNmHFqRUm3lQ2VKMLq56FhKECgYEA0IFE\neHzyt7izGGFIiYhpEnqfc/OhxC6VqaHOMbPsCgK0f5+5awObJhlrwWw+PEczBW13\naHTaswuw5EYGamJc7g9brnHLrBVXfKvYYSqdvShp3bQqnWh9MTzjj0IYv5gBeMtA\n0qte+gV5/NUGrDxKyzGUTshXx5dVf90JRC7fLeECgYBS66NFuHKM/e+n7MmoIqT5\nJIeEmptMLmrCkU1Qtznx1FUt8LO0oLR4aXySv0+ubsV8fzH7BxXKy75l0qSLkQBM\nQrB2IuO1J6cSuhHJ1sqpTwVuKMRCgq7nKcEKFRsW+sAXL/vruA6aNht0l4x6fkJ4\nJKLM742oNG4csbTxqxeeoQKBgFZE5fukVxjFBvUTa1vcYP0QV2E2cLwnOi1RkWrn\nMsaBkAUuJR2uBEejRP5mtulh3C5muH0zvDlQoQQSJR1nTWQCXsCyvL6apfQjdgfe\nBh351rOwk+FFFmeE9fKUOoErd5BvKIcB+O4hzfNagMRKvfeMr/xY0Fj4uJuK7QaV\nDiqBAoGAXmp8xXZGmwOj0wBrql2hvvsCNkWk1AyR3USsFLwFnG0Vk922/lkRnRac\nNXg0bsu6UW+xbNobv5J942C6RLnN73uQ7cqhpouzahv4O9tffp/A4Kp7mZ+3DfEL\n/xRqgDClq2tEo9nxMQg9pEnMEtMdkjIgGUOhBpkBhyxIWB0BKNs=\n-----END RSA PRIVATE KEY-----",
    "request": {
        "name": "Clark Kent",
        "type": "overall"
    }
}
```
In Response we get
```
{
    "request": "eyJuYW1lIjogIkNsYXJrIEtlbnQiLCAidHlwZSI6ICJvdmVyYWxsIn0=.fITD9WjteFldTtbiLwD6S6212XRTEK2gPWDiuCzywQ6euqKDtEITXIUqp2WSOZ1s7BC7wy3zMoT7zrykwzuAzKUelwWor7HSP/ioUD98ip019/oxnCR66hMzH9qARtND1/cQ12KXl1yGahsm9I49dbBg6cBk5pktNbpVULyYtBX58oCnVGXNRKcXM44mNeR34FOO4ips2vNVQIGp4CXw5zKZ2wB2lhzRt2Ngoq6KtTXl7J98pV2xIu1dTyYGjugas3eNiRhA44JvOIQH79RHDluSpw7X2CVdgxy18TzJuaQrGNPAqVARnsBoD3prB8cCPyc8mMdkQafmAp2fzA4h4Q=="
}
```
and now we can call http://localhost:8080/api/mystats
with the body
```
{
    "request": "eyJuYW1lIjogIkNsYXJrIEtlbnQiLCAidHlwZSI6ICJvdmVyYWxsIn0=.fITD9WjteFldTtbiLwD6S6212XRTEK2gPWDiuCzywQ6euqKDtEITXIUqp2WSOZ1s7BC7wy3zMoT7zrykwzuAzKUelwWor7HSP/ioUD98ip019/oxnCR66hMzH9qARtND1/cQ12KXl1yGahsm9I49dbBg6cBk5pktNbpVULyYtBX58oCnVGXNRKcXM44mNeR34FOO4ips2vNVQIGp4CXw5zKZ2wB2lhzRt2Ngoq6KtTXl7J98pV2xIu1dTyYGjugas3eNiRhA44JvOIQH79RHDluSpw7X2CVdgxy18TzJuaQrGNPAqVARnsBoD3prB8cCPyc8mMdkQafmAp2fzA4h4Q=="
}
```
we get in response:
```
{
    "ranking": 1
}
```

If we try to check the rank of Romi Ron in Tel Aviv we sign a request with the name Romi Ron and the type city
```
"request": {
        "name": "Romi Ron",
        "type": "city"
    }
```
after calling _mystats_ we get the response:
```
{
    "ranking": 2
}
```

we can do the same with
```
"request": {
        "name": "Dan Dean",
        "type": "age"
    }
```
and we get in response (after signnig and running _mystats of course)

```
{
    "ranking": 2
}
```