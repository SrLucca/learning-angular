import { Component, OnInit } from '@angular/core';
import {SharedService} from 'src/app/shared.service';

@Component({
  selector: 'app-show-dep',
  templateUrl: './show-dep.component.html',
  styleUrls: ['./show-dep.component.css']
})
export class ShowDepComponent implements OnInit {

  constructor(private service:SharedService) { }

  DepartamentList:any = [];


  ModalTitle:string;
  ActivateAddEditDepComp:boolean=false;
  dep:any;

  ngOnInit(): void {
    this.refreshDepList();
  }

  addClick(){
    this.dep={
      DepartamentId:0,
      DepartamentName:""
    }
    this.ModalTitle = "Add Departament";
    this.ActivateAddEditDepComp = true;
  }


  refreshDepList(){
    this.service.getDepList().subscribe(data=>{
      this.DepartamentList=data;
    });
  }
  
}
