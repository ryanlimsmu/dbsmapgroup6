import React from 'react'
import '../../css/ReqTable.css'

const ReqTable = ( { isHomePage, requests } ) => {
  return (
    <div>
      <table>
        <tr>
          { !isHomePage && <th><input type="checkbox"></input></th> }
          <th>Request date</th>
          <th>{ isHomePage ? "Requester Company Name" : "Company Name"}</th>
          <th>Carbon Price</th>
          <th>Carbon Quantity</th>
          <th>Requesting Reason</th>
          <th>Request Type</th>
        </tr>
      <tbody>
        {requests.map((req) => ( 
          <tr>
            { !isHomePage && <td></td>}
            <td>{req.request_date}</td>
            <td>{req.company_name}</td>
            <td>{req.carbon_price}</td>
            <td>{req.carbon_qty}</td>
            <td>{req.requesting_reason}</td>
            <td>{req.request_type}</td>
          </tr>
          ))}
      </tbody>
    </table>
   </div>
  )
}

export default ReqTable