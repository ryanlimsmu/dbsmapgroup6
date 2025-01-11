import React from 'react'
import Req_table from './requests/ReqTable'

const Requests = () => {
  // dummy data 
  const requests = [
    {
        request_date: "11/07/2020",
        company_name: "ABC",
        carbon_price: 11,
        carbon_qty: 13,
        requesting_reason: "ABCD",
        request_type: "Buy"
    }
  ]

  return (
    <Req_table isHomePage={ false } requests={ requests }/>
  )
}

export default Requests