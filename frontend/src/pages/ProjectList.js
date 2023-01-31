import React,{ useEffect, useState } from "react";
import axios from "axios";

function ProjectList(){
    const url = 'http://localhost:8000/projects/project_list/';

    const [prjList, setPrjList] = useState([]);

    const projectList = useEffect(() => {
        axios.get(url)
            .then(result => {
                console.log(result.data.projects);
                setPrjList(result.data.projects);
            })
            .catch(error => {
                console.log(error);
            });
    }, []);
        
    return (
        <div>
            {projectList => {
                prjList.map(project => (
                    <p>{project}</p>
                ))
            }}
        </div>
    );
}

export default ProjectList;