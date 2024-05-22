

import { useState, useEffect, createContext} from "react";


export let UserContext = createContext();

export default function UserContextProvider(props) {
    let[Usertoken,Settoken]=useState(null)
    let[Usertoken2,Settoken2]=useState(null)
    let[dataa,setdataa]=useState(null)
 /////////////////////////////
  const [email, setEmailuser] = useState("");
    //   let data=null
    // useEffect(()=>{
    //     if(Usertoken!=null){
    //    data= jwtDecode(Usertoken)
    //       console.log(data);
    //     }
        
    //     },[])
   
  return (
    <UserContext.Provider
      value={{
        Usertoken,
        Settoken,
        email,
        setEmailuser,
        // data,
        Usertoken2,
        Settoken2,
        dataa,
        setdataa
      }}
    >
      {props.children}
    </UserContext.Provider>
  );
}
