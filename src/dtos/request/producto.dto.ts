import {
  IsArray,
  IsDecimal,
  IsNotEmpty,
  IsNumber,
  IsOptional,
  IsPositive,
  IsString,
} from "class-validator";

export class CrearProductoDto {
  @IsString()
  @IsNotEmpty()
  productoNombre: string;

  @IsPositive()
  @IsDecimal()
  productoPrecio: number;

  @IsNumber()
  @IsPositive()
  productoCantidad: number;

  @IsOptional()
  @IsArray()
  productoFoto?: Array<string>; // string[]
}
