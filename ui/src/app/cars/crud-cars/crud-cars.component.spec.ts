import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CrudCarsComponent } from './crud-cars.component';

describe('CrudCarsComponent', () => {
  let component: CrudCarsComponent;
  let fixture: ComponentFixture<CrudCarsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CrudCarsComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CrudCarsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
