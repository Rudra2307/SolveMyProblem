import React,{Text,useEffect} from 'react';
import * as Location from 'expo-location';

import CameraPage from '../components/camerapage';

export default function Home({ navigation }) {
    useEffect(() => {

        (async () => {
            try {
                let { status } = await Location.requestForegroundPermissionsAsync();
                if (status !== 'granted') {
                    setErrorMsg('Permission to access location was denied');
                }
                console.log(status);
                
            } catch (error) {
                console.log("log",error);
            }

        })();
    },[]);
    
    return (

        // <Text>{"hello"}</Text>
        <CameraPage navigation={navigation} />
    );

};